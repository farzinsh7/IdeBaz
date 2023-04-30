from django.contrib import admin
from .models import Article, Tags, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'title', 'category_to_str', 'status')
    list_filter = ('publish', 'status', 'category')
    search_fields = ('title', 'description')
    ordering = ['-publish']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tags)