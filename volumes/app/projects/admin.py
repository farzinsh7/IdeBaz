from django.contrib import admin
from .models import Project, Category, ProjectGallery


class ProjectGalleryAdmin(admin.TabularInline):
    model = ProjectGallery
    extra = 1
    max_num = 10

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectGalleryAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}