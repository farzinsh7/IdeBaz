# Generated by Django 4.2 on 2023-05-06 10:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
