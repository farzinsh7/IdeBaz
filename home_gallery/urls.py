from django.urls import path
from home_gallery.views import home_iformation, HeaderView, FooterView

app_name = 'homepage'

urlpatterns = [
    path('', home_iformation, name='information'),
    path('header/', HeaderView.as_view(), name='header'),
    path('footer/', FooterView.as_view(), name='footer'),
]