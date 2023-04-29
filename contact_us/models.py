from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()


    def __str__(self):
        return self.subject


class ContactUS(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()
    map = models.URLField()

    def __str__(self):
        return self.title
    

    