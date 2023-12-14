from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Color
from django.contrib.auth.mixins import LoginRequiredMixin

import json
from django.http import HttpResponse
from django.shortcuts import render

import os
from django.core.files import File
import base64
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from .models import XmasCard


def home(request):
    return render(request, 'joulukortti/home.html')

def canvas(request):
    if request.user.is_authenticated:
        colors = request.user.color_set.all()  # Get colors specific to the user
    else:
        # Get all unique color objects for unauthenticated users
        colors = Color.objects.values('hex_value').annotate(count=Count('id')).order_by()
    return render(request, 'joulukortti/canvas.html', {'colors': colors})

@login_required
def gallery(request):
    xmas_cards = XmasCard.objects.all()
    return render(request, 'joulukortti/gallery.html', {'xmas_cards': xmas_cards})


@csrf_exempt
def save_drawing(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            image_data = data['image']

            # Decode the base64 image
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]

            # Use the drawing's name for the file name, replacing spaces with underscores and adding the extension
            filename = f"{name.replace(' ', '_')}.{ext}"

            # Ensure filename uniqueness to avoid overwriting existing files
            filename = get_unique_filename(filename)

            image = ContentFile(base64.b64decode(imgstr), name=filename) # name=f'{uuid.uuid4()}.{ext}'

            # For simplicity, create a user if it doesn't exist
            user, created = User.objects.get_or_create(username='December') # Replace with appropriate username

            # Create a new XmasCard instance
            xmas_card = XmasCard(name=name, drawing=image, user=user)
            xmas_card.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error'}, status=400)

def get_unique_filename(filename):
    """
    Generates a unique filename by appending a counter to the filename
    if a file with the same name already exists.
    """
    original_filename = filename
    counter = 1
    while os.path.exists(os.path.join('/', filename)):  # Replace with your media directory
        name, ext = os.path.splitext(original_filename)
        filename = f"{name}_{counter}{ext}"
        counter += 1
    return filename

class ColorListView(LoginRequiredMixin, ListView):
    model = Color
    template_name = 'joulukortti/colors/color_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Color.objects.filter(users=self.request.user)
        else:
            return Color.objects.none()

class ColorCreateView(LoginRequiredMixin, CreateView):
    model = Color
    fields = ['name', 'hex_value']
    template_name = 'joulukortti/colors/color_form.html'
    success_url = reverse_lazy('color_list')

    def form_valid(self, form):
        color = form.save(commit=False)
        color.save()
        color.users.add(self.request.user)  # Link color to the current user
        return super().form_valid(form)

class ColorUpdateView(LoginRequiredMixin, UpdateView):
    model = Color
    fields = ['name', 'hex_value']
    template_name = 'joulukortti/colors/color_form.html'
    success_url = reverse_lazy('color_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(users=self.request.user)

class ColorDeleteView(LoginRequiredMixin, DeleteView):
    model = Color
    template_name = 'joulukortti/colors/color_confirm_delete.html'
    success_url = reverse_lazy('color_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(users=self.request.user)
