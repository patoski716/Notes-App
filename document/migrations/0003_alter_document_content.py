# Generated by Django 4.2.8 on 2023-12-10 15:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20200729_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
