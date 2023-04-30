from django.urls import path
from .views import  ArticleListView

app_name = 'article'

urlpatterns = [
    path('article/', ArticleListView.as_view(), name='list_view'),
]