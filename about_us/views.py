from django.shortcuts import render
from .models import AboutUs, OurSkills, Services

# Create your views here.

def about_us(request):
    return render(request, 'about.html')
