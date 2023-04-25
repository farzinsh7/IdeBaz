from django.shortcuts import render
from .models import AboutUs, OurSkills, Services


# Create your views here.

def about_us(request):
    about = AboutUs.objects.all().first()
    services = Services.objects.all()
    skills = OurSkills.objects.all()
    context = {
        'about': about,
        'services': services,
        'skills': skills,
    }
    return render(request, 'about.html', context)
