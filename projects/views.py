from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project ,Category


class ProjectListView(ListView):
    model = Project
    queryset = Project.objects.published()
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    queryset = Project.objects.filter(status='p')
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(status=True)
        return context