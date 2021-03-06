# Generated by Django 4.0 on 2022-02-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0016_rename_recommended_animetitans_customized_lists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animes_animetitans',
            name='Type',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='country',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='duration',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='episodes',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='image',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='rating',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='season',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='slug',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='status',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='story',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='studio',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='title',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='trailer',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='url',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='year',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='episode_animetitans',
            name='number',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='episode_animetitans',
            name='slug',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='episode_animetitans',
            name='url',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
