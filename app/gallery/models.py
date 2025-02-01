from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class GalleryNewShapes(models.Model):
    image = models.ImageField(
        upload_to='gallery_photos/',
        verbose_name='Изоброжение новых фигур'
    )

    def __str__(self):
        return f"Photo {self.id}"

    class Meta:
        verbose_name = 'Галерея новой фигуры'
        verbose_name_plural = 'Галерея новых фигур'

class GalleryOshTour(models.Model):
    title = models.CharField(
        max_length=135,
        verbose_name='Заголовок Изображений'
    )
    image = models.ImageField(
        upload_to='gallery_images/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея Ош Тур'
        verbose_name_plural = 'Галерея Ош Тура'


class GalleryArchivalPhotos(models.Model):
    image = models.ImageField(
        upload_to='gallery_photos/'
    )

    def __str__(self):
        return f"Photo {self.id}"  

    class Meta:
        verbose_name = 'Галерея Архивного Фото'
        verbose_name_plural = 'Галерея Архивных Фото'
