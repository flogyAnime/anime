# Generated by Django 4.0 on 2022-02-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_profile_use_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='use_profile_picture',
            field=models.BooleanField(default=False),
        ),
    ]
