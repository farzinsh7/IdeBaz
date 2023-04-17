import os
from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}"
    return f"Home/gallery/{final_name}"


# Create your models here.
class HomeGallery(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True)
    main_img = models.ImageField(upload_to=upload_gallery_image_path)
    thumbnail = models.ImageField(upload_to=upload_gallery_image_path)


    def __str__(self):
        return self.title


