from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView
from .models import ContactForm, ContactUS
from .forms import ContactFormClass
from home_gallery.models import Information


# Create your views here.
class ContactUs(CreateView):
    model = ContactForm
    form_class = ContactFormClass
    success_url = reverse_lazy('contact_page:contact_us')
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactUS.objects.all().first()
        context['info'] = Information.objects.all().first()
        return context