from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from account.models import User
from tinymce.models import HTMLField
# from django.contrib.contenttypes.fields import GenericRelation
# from django.urls import reverse
# from comment.models import Comment
# from ckeditor_uploader.fields import RichTextUploadingField



class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    # position = models.IntegerField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('account:category')


class Tags(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('account:tags')


# class IPAddress(models.Model):
#     ip_address = models.GenericIPAddressField(verbose_name="آدرس ای پی")


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles')
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ManyToManyField(Category, related_name='articles')
    tags = models.ManyToManyField(Tags, related_name='articles', blank=True)
    description = HTMLField()
    image = models.ImageField(upload_to='article')
    image_thumbnail = models.ImageField(upload_to='article')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)
    # comments = GenericRelation(Comment)
    # hits = models.ManyToManyField(IPAddress, through="BlogHit", blank=True, related_name='hits')

    # class Meta:
    #     verbose_name = 'مقاله'
    #     verbose_name_plural = 'مقالات'
    #     ordering = ['-publish']

    def __str__(self):
        return self.title

    # def j_publish(self):
    #     return jalali_converter(self.publish)

    # j_publish.short_description = 'زمان انتشار'

    # def get_absolute_url(self):
    #     if self.status == 'p':
    #         return reverse('blog:blog_detail', args=[self.slug])
    #     else:
    #         return reverse('account:panel')

    def thumbnail_tag(self):
        return format_html(
            "<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.image_thumbnail.url))

    thumbnail_tag.short_description = "عکس بندانگشتی"

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.all()])

    category_to_str.short_description = "دسته‌بندی"

    objects = ArticleManager()


# class BlogHit(models.Model):
#     blogs = models.ForeignKey(Article, on_delete=models.CASCADE)
#     ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)