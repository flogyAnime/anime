# Generated by Django 4.0 on 2022-01-31 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0014_alter_animes_animetitans_categories_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suggestion_animetitans',
            new_name='Recommended_animetitans',
        ),
    ]