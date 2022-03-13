# Generated by Django 4.0 on 2022-01-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0014_alter_animes_animetitans_categories_and_more'),
        ('accounts', '0002_profile_watchnow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite', to='animetitans.Animes_animetitans'),
        ),
        migrations.AddField(
            model_name='profile',
            name='wantWatch',
            field=models.ManyToManyField(related_name='wantWatch', to='animetitans.Animes_animetitans'),
        ),
        migrations.AddField(
            model_name='profile',
            name='watched',
            field=models.ManyToManyField(related_name='watched', to='animetitans.Animes_animetitans'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='watchNow',
            field=models.ManyToManyField(related_name='watchNow', to='animetitans.Animes_animetitans'),
        ),
    ]
