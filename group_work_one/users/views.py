from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from joulukortti.models import Color


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)

            # Assign all colors to the new user
            all_colors = Color.objects.all()
            for color in all_colors:
                color.users.add(new_user)

            return redirect('home')
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)
        


