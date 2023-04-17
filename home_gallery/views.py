from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeGallery, Information


# Create your views here.

# class InformationListView(ListView):
#     model = Information
#     queryset = Information.objects.first()
#     context_object_name = "info"
#     template_name = "home.html"


def home_iformation(request):
    information = Information.objects.first()
    gallery = HomeGallery.objects.all()
    context = {
        'info': information,
        'gallery': gallery,
    }
    return render(request, 'home.html', context)