from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import HomeGallery, Information
from contact_us.models import ContactForm


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

# class HomeInformation(CreateView):
#     model = ContactForm
#     fields = ['name', 'email', 'subject', 'message']
#     success_url = reverse_lazy('homepage:information')
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['gallery'] = HomeGallery.objects.all()
#         return context

