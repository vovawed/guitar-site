# Generated by Django 2.2.2 on 2019-06-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190606_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvideo',
            name='video_id',
            field=models.TextField(verbose_name='Vimeo id'),
        ),
    ]
