# Generated by Django 4.0 on 2022-01-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0011_alter_animes_animetitans_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion_animetitans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ManyToManyField(blank=True, null=True, to='animetitans.Animes_animetitans')),
            ],
        ),
    ]
