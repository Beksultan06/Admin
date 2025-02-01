from django.db import models

# Create your models here.

class We_Invite_To_View(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Мы предлагаем к просмотру"
    )
    # Места для просмотра
    title_place = models.CharField(
        max_length=255,
        verbose_name="Заголовок для места просмотра"
    )
    description_place = models.CharField(
        max_length=255,
        verbose_name="Описание для места просмотра"
    )
    date_place = models.DateField(
        verbose_name="Дата места просмотра"
    )
    image_place = models.ImageField(
        upload_to='base/',
        verbose_name="Изображение для места просмотра"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Места для просмотра"
        verbose_name_plural = "Места для просмотра"

class Gallery(models.Model):
    title_gallery = models.CharField(   
        max_length=255,
        verbose_name="Заголовок для галереи"
    )
    photo = models.ImageField(
        upload_to='base/',
        verbose_name="Фотография"
    )
    def __str__(self):
        return self.title_gallery

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

