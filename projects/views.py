from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Project, Category
from django.http import JsonResponse


# class ProjectListView(ListView):
#     model = Project
#     queryset = Project.objects.published()
#     template_name = 'project_list.html'
#     context_object_name = 'projects'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.all()
#         return context

class ProjectListView(TemplateView):
    template_name = 'project_list.html'


class ProjectJsonView(View):
    def get(self, *args, **kwargs):
        upper = kwargs.get('num_projects')
        lower = upper - 3
        projects = list(Project.objects.values()[lower:upper])
        projects_size = len(Project.objects.published())
        max_size = True if upper >= projects_size else False
        category = list(Category.objects.values())
        return JsonResponse({'projects': projects, 'max': max_size, 'category': category}, safe=False)


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    queryset = Project.objects.filter(status='p')
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(status=True)
        return context
