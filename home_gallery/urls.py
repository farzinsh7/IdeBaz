from django.urls import path
from home_gallery.views import home_iformation, InformationListView

app_name = 'homepage'

urlpatterns = [
    path('', home_iformation, name='information'),
    path('header/', InformationListView.as_view(), name='header'),
    # path('footer/', InformationListView.as_view(), name='header'),
]