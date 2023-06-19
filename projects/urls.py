from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectJsonView

app_name = 'project'

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='list_view'),
    path('project-json/<int:num_projects>/', ProjectJsonView.as_view(), name='project-json-view'),
    path('Projects/<slug:slug>', ProjectDetailView.as_view(), name='detail_view'),
]