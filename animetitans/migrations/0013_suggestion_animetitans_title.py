# Generated by Django 4.0 on 2022-01-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0012_suggestion_animetitans'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion_animetitans',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]