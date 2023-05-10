from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . models import Article, Category, Tags
from datetime import datetime, timedelta

# Create your views here.


class ArticleListView(ListView):
    queryset = Article.objects.published()
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article'
    paginate_by = 1


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    queryset = Article.objects.filter(status='p')
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tags.objects.filter(status=True)
        context['category'] = Category.objects.filter(status=True)
        return context


class TagList(ListView):
    model = Tags
    paginate_by = 6
    template_name = 'tags.html'

    def get_queryset(self):
        global tag
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(Tags.objects.all(), slug=slug)
        return tag.articles.published()
