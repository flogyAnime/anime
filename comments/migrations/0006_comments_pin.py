# Generated by Django 4.0 on 2022-02-06 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_alter_comments_added_date_alter_comments_dislike_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='pin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
