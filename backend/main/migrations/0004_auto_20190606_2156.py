# Generated by Django 2.2.2 on 2019-06-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_studentvideo_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentvideo',
            name='iframe',
        ),
        migrations.AddField(
            model_name='studentvideo',
            name='video_id',
            field=models.TextField(default=1, verbose_name='Vimeo id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentvideo',
            name='title',
            field=models.BigIntegerField(max_length=100, verbose_name='Назва'),
        ),
    ]