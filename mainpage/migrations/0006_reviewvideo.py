# Generated by Django 4.1 on 2023-12-10 07:52

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_projectvideo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок видео')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание видео')),
                ('url', embed_video.fields.EmbedVideoField(verbose_name='Ссылка на видео')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
        ),
    ]
