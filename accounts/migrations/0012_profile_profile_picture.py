# Generated by Django 4.0 on 2022-02-03 03:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_profile_main_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='<django.db.models.query_utils.DeferredAttribute object at 0x000001DAFE4399C0>/profile_picture/'),
            preserve_default=False,
        ),
    ]
