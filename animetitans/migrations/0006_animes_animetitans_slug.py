# Generated by Django 4.0 on 2022-01-08 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0005_rename_episode_number_animes_animetitans_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='animes_animetitans',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]