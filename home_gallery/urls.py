from django.urls import path
from .views import  HeaderView, FooterView, HomeInformation

app_name = 'homepage'

urlpatterns = [
    path('', HomeInformation.as_view(), name='information'),
    path('header/', HeaderView.as_view(), name='header'),
    path('footer/', FooterView.as_view(), name='footer'),
]