from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image_icon = models.ImageField("service") 

    def __str__(self):
        return self.title


class OurSkills(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.title