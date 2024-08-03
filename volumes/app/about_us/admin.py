from django.contrib import admin
from .models import AboutUs, Services, OurSkills

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(OurSkills)
admin.site.register(Services)