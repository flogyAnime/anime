# Generated by Django 4.0 on 2022-01-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_favorite_alter_profile_wantwatch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
