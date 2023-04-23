from django.urls import path
from .views import about_us

app_name = 'aboutpage'

urlpatterns = [
    path('about-us/', about_us, name='about'),
]