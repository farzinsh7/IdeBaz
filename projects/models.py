from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class ProjectManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Project(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    client = models.CharField(max_length=150, default='user')
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ManyToManyField(Category, related_name='projects')
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='project')
    website = models.CharField(max_length=150, null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)


    def __str__(self):
        return self.title

    objects = ProjectManager()

class ProjectGallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='project-gallery')
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, related_name='galleries')

    def __str__(self):
        return self.title
