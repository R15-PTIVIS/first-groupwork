from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from joulukortti.models import XmasCard
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import XmasCard

import os
import base64
from django.core.files import File


def home(request):
    return render(request, 'joulukortti/home.html')

def canvas(request):
    return render(request, 'joulukortti/canvas.html')

def gallery(request):
    xmas_cards = XmasCard.objects.all()
    return render(request, 'joulukortti/gallery.html', {'xmas_cards': xmas_cards})

def save_drawing(request):
    if request.method == 'POST':
        data = request.json()
        name = data.get('name')
        image_data = data.get('image_data')

        # For simplicity, create a user if it doesn't exist
        user, created = User.objects.get_or_create(username='December')

        # Create a new XmasCard object and save it to the database
        xmas_card = XmasCard(name=name, drawing=image_data, user=user)
        xmas_card.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

def save_image(request):
    # Specify the path to your PNG image file
    image_path = "joulukortti/static/drawing.png"

    # Check if the file exists
    if os.path.exists(image_path):
        # Open the image file
        with open(image_path, 'rb') as image_file:
            # Create a File object from the image data
            image_data = File(image_file)

            # For simplicity, create a user if it doesn't exist
            user, created = User.objects.get_or_create(username='December')

            # Create a new XmasCard object and save it to the database
            xmas_card = XmasCard(name='TestCard', drawing=image_data, user=user)
            xmas_card.save()

            # Move the file cursor to the beginning of the file
            image_file.seek(0)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Image file not found'})