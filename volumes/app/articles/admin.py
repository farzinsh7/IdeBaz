from django.contrib import admin
from .models import Article, Tags, Category
from . import models


# class ArticleCategoryAdmin(admin.TabularInline):
#     model = Category
    # extra = 1
    # max_num = 10


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    # inlines = [ArticleCategoryAdmin]
    autocomplete_fields = ["author"]
    prepopulated_fields = {"slug": ["title"]}
    list_display = ('thumbnail_tag', 'title', 'category_to_str', 'status')
    list_filter = ('publish', 'status', 'category')
    search_fields = ('title', 'description')
    ordering = ['-publish']


admin.site.register(Category)
admin.site.register(Tags)