# Generated by Django 4.0 on 2022-01-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animes_animetitans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
                ('trailer', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=1000)),
                ('story', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1000)),
                ('studio', models.CharField(max_length=1000)),
                ('year', models.CharField(max_length=1000)),
                ('duration', models.CharField(max_length=1000)),
                ('season', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=1000)),
                ('Type', models.CharField(max_length=1000)),
                ('episodes', models.CharField(max_length=1000)),
                ('categories', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Episode_animetitans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.CharField(max_length=1000)),
                ('number', models.CharField(max_length=1000)),
                ('download', models.CharField(max_length=1000)),
                ('watch', models.CharField(max_length=10000)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
    ]
