from django.urls import path
from .views import  ArticleListView, ArticleDetailView, TagList

app_name = 'article'

urlpatterns = [
    path('article/', ArticleListView.as_view(), name='list_view'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='detail_view'),
    path('tags/<slug:slug>', TagList.as_view(), name='tag_view'),
]