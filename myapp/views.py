from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/home.html', {'form': form})

def display(request):
    registrations = Registration.objects.all()
    return render(request, 'myapp/display.html', {'registrations': registrations})
