from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Color

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
    return render(request, 'joulukortti/canvas.html')

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

class ColorListView(ListView):
    model = Color
    template_name = 'joulukortti/colors/color_list.html'

class ColorCreateView(CreateView):
    model = Color
    fields = ['name', 'hex_value']
    template_name = 'joulukortti/colors/color_form.html'
    success_url = reverse_lazy('color_list')

class ColorUpdateView(UpdateView):
    model = Color
    fields = ['name', 'hex_value']
    template_name = 'joulukortti/colors/color_form.html'
    success_url = reverse_lazy('color_list')

class ColorDeleteView(DeleteView):
    model = Color
    template_name = 'joulukortti/colors/color_confirm_delete.html'
    success_url = reverse_lazy('color_list')
