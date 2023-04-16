from django.urls import path
from home_gallery.views import gallery

app_name = 'homepage'

urlpatterns = [
    path('', gallery, name='gallery'),
]