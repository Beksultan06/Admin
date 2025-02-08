from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Managers(models.Model):
    full_name = models.CharField(verbose_name="Фио", max_length=255)
    job_title = models.CharField(verbose_name="Должность", max_length=255)
    image = models.ImageField(verbose_name="Фото", upload_to="managers_img/")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"


class Structure_admins(models.Model):
    title = models.CharField(max_length=255, verbose_name="Структура администрации")
    image = models.ImageField(verbose_name="Фото", upload_to="managers_img/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Структура администрации"
        verbose_name_plural = "Структуры администрации"


class Schedule(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    date = models.TimeField(verbose_name="Время")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class Catalog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Описание")
    date = models.TimeField(verbose_name="Время")
    image = image = models.ImageField(verbose_name="Фото", upload_to="managers_img/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"
