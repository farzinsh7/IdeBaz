from django.urls import path
from home_gallery.views import home_iformation

app_name = 'homepage'

urlpatterns = [
    path('', home_iformation, name='information'),
]