from django.db import models


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

