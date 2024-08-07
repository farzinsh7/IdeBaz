# Generated by Django 5.0.6 on 2024-08-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.URLField(blank=True, null=True)),
                ('main_img', models.ImageField(upload_to='gallery')),
                ('thumbnail', models.ImageField(upload_to='gallery/thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('logo', models.ImageField(null=True, upload_to='core')),
                ('logo_hover', models.ImageField(null=True, upload_to='core')),
                ('description', models.TextField()),
                ('facebook', models.SlugField(null=True)),
                ('instagram', models.SlugField(null=True)),
                ('pinterest', models.SlugField(null=True)),
                ('linkedin', models.SlugField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
            ],
        ),
    ]
