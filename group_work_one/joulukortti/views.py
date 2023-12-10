from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from joulukortti.models import XmasCard


def home(request):
    return render(request, 'joulukortti/home.html')

def canvas(request):
    return render(request, 'joulukortti/canvas.html')

def gallery(request):
    xmas_cards = XmasCard.objects.all()
    return render(request, 'joulukortti/gallery.html', {'xmas_cards': xmas_cards})