# Generated by Django 4.0 on 2022-01-11 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0009_categories_animetitans_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode_animetitans',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animetitans.animes_animetitans'),
        ),
    ]
