from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeGallery, Information


# Create your views here.

class HeaderView(ListView):
    model = Information
    queryset = Information.objects.first()
    context_object_name = "info"
    template_name = "base/shared/header.html"


class FooterView(ListView):
    model = Information
    queryset = Information.objects.first()
    context_object_name = "info"
    template_name = "base/shared/footer.html"


def home_iformation(request):
    gallery = HomeGallery.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'home.html', context)

