# Generated by Django 4.0 on 2022-02-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_profile_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tag',
            field=models.CharField(blank=True, default='متابع انمي', max_length=50, null=True),
        ),
    ]
