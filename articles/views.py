from django.shortcuts import render
from django.views.generic import ListView
from . models import Article, Category, Tags

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.published()
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article'
    paginate_by = 1