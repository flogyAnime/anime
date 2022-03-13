# Generated by Django 4.0 on 2022-01-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0008_episode_animetitans_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories_animetitans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=1000)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='episode_animetitans',
            name='download',
        ),
        migrations.RemoveField(
            model_name='episode_animetitans',
            name='watch',
        ),
        migrations.AddField(
            model_name='animes_animetitans',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='animes_animetitans',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='D_4shared',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='D_googledrive',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='D_mega',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='D_mp4upload',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='D_other',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='D_solidfiles',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='W_4shared',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='W_googledrive',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='W_mega',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='W_mp4upload',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='W_solidfiles',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='episode_animetitans',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='Type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.RemoveField(
            model_name='animes_animetitans',
            name='categories',
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='country',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='duration',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='episodes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='rating',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='season',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='slug',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='status',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='story',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='studio',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='trailer',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animes_animetitans',
            name='year',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='episode_animetitans',
            name='slug',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animes_animetitans',
            name='categories',
            field=models.ManyToManyField(to='animetitans.Categories_animetitans'),
        ),
    ]