# Generated by Django 4.0 on 2022-02-03 08:22

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(upload_to=accounts.models.getcurrentusername),
        ),
    ]
