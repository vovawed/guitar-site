# Generated by Django 2.2.1 on 2019-05-11 18:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('iframe', models.TextField(verbose_name='iFrame')),
            ],
            options={
                'verbose_name': 'відео учнів',
                'verbose_name_plural': 'відео учнів',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('image', models.ImageField(help_text='Відношення сторін - 16:9', upload_to='images', verbose_name='Картинка')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
                ('text_preview', models.TextField(help_text='До 450 символів', max_length=400, verbose_name="Прев'ю")),
                ('date', models.DateTimeField(verbose_name='Час публікації')),
                ('tags', models.ManyToManyField(to='main.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'стаття',
                'verbose_name_plural': 'статті',
            },
        ),
    ]
