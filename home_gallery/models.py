import os
from django.db import models


# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext


# def upload_gallery_image_path(instance, filename):
#     name, ext = get_filename_ext(filename)
#     final_name = f"{instance.id}-{instance.title}"
#     return f"Home/gallery/{final_name}"


# Create your models here.
class HomeGallery(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(null=True, blank=True)
    main_img = models.ImageField(upload_to="gallery")
    thumbnail = models.ImageField(upload_to="gallery/thumbnail")

    def __str__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(max_length=150)
    logo = models.ImageField(null=True, upload_to="core")
    logo_hover = models.ImageField(null=True, upload_to="core")
    description = models.TextField()
    facebook = models.SlugField(null=True)
    instagram = models.SlugField(null=True)
    pinterest = models.SlugField(null=True)
    linkedin = models.SlugField(null=True)
    email = models.EmailField()
    address = models.TextField(null=True)
    phone = models.CharField(max_length=11,null=True)

    def __str__(self):
        return self.title
    
