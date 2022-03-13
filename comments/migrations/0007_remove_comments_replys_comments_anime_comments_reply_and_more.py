# Generated by Django 4.0 on 2022-02-10 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animetitans', '0017_alter_animes_animetitans_type_and_more'),
        ('comments', '0006_comments_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='replys',
        ),
        migrations.AddField(
            model_name='comments',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animetitans.animes_animetitans'),
        ),
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ManyToManyField(blank=True, null=True, related_name='+', to='comments.Replys'),
        ),
        migrations.AddField(
            model_name='replys',
            name='from_Comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comments'),
        ),
        migrations.AddField(
            model_name='replys',
            name='pin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]