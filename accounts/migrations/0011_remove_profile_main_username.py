# Generated by Django 4.0 on 2022-01-29 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_main_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='main_username',
        ),
    ]
