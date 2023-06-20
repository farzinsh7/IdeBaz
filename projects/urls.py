from django.urls import path
from .views import ProjectListView, ProjectDetailView

app_name = 'project'

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='list_view'),
    path('Projects/<slug:slug>', ProjectDetailView.as_view(), name='detail_view'),
]