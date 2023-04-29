from django.urls import path
from .views import  ContactUs

app_name = 'contact_page'

urlpatterns = [
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
]