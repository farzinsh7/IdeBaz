from django.urls import path
from .views import ProjectListView

app_name = 'project'

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='list_view'),
]