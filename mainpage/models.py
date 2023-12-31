from django.core.validators import FileExtensionValidator
from django.db import models
from embed_video.fields import EmbedVideoField


class Stair(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок изображения')
    image = models.ImageField(upload_to='stairs', verbose_name='Изображение')

    def __str__(self):
        return self.title


class Shelter(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок изображения', unique=True, null=False)
    image = models.ImageField(upload_to='shelters', verbose_name='Изображение', unique=True, null=False)

    def __str__(self):
        return self.title


class Fence(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок изображения', unique=True, null=False)
    image = models.ImageField(upload_to='fences', verbose_name='Изображение', unique=True, null=False)

    def __str__(self):
        return self.title


class Pergola(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок изображения', unique=True, null=False)
    image = models.ImageField(upload_to='pergolas', verbose_name='Изображение', unique=True, null=False)

    def __str__(self):
        return self.title


class ProjectVideo(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='Заголовок видео')
    description = models.TextField(max_length=1000, verbose_name='Описание видео', blank=True)
    url = EmbedVideoField(verbose_name='Ссылка на видео')
    added = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return self.title


class ReviewVideo(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='Заголовок видео')
    description = models.TextField(max_length=1000, verbose_name='Описание видео', blank=True)
    url = EmbedVideoField(verbose_name='Ссылка на видео')
    added = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return self.title