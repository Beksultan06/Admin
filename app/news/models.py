from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class News(models.Model):
    # Новости
    title_news = models.CharField(
        max_length=100, verbose_name='Заголовок новостей страницы "Новости"'
    )
    description_news = RichTextField(
        verbose_name='Описание новостей страницы "Новости"'
    )
    date_news = models.DateTimeField(verbose_name='Дата новостей страницы "Новости"')
    image_news = models.ImageField(upload_to="news/")
    first_paragraph = RichTextField(
        verbose_name='Первый абзац детальный просмотр новостей страницы "Новости"'
    )
    second_paragraph = RichTextField(
        verbose_name='Второй абзац детальный просмотр новостей страницы "Новости"'
    )
    general_paragraph = RichTextField(
        verbose_name='Общий абзац детальный просмотр новостей страницы "Новости"'
    )

    def __str__(self):
        return self.title_news

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Media(models.Model):
    # CМИ
    title_media = models.CharField(
        max_length=100, verbose_name='Заголовок СМИ страницы "Новости"'
    )
    description_media = RichTextField(verbose_name='Описание СМИ страницы "Новости"')
    date_media = models.DateTimeField(verbose_name='Дата СМИ страницы "Новости"')
    image_media = models.ImageField(upload_to="news/")

    def __str__(self):
        return self.title_media

    class Meta:
        verbose_name = "СМИ"
        verbose_name_plural = "СМИ"


# Страница новостей ноокатского района
class NewsNok(models.Model):
    title = RichTextField()
    description = RichTextField()
    date = models.CharField(max_length=225)
    photo = models.ImageField(upload_to="news-nok/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость Нокатская область"
        verbose_name_plural = "Новости Нокатская область"


# Лучшие туристические места ноокатского района
class TourismNok(models.Model):
    title = RichTextField()
    description = RichTextField()
    image = models.ImageField(upload_to="tourism-nok/")


# ноокатская районая администрация
class AboutNok(models.Model):
    description = RichTextField()
    image = models.ImageField(upload_to="about-nok/")

    def __str__(self):
        return "О Нокатской область"

    class Meta:
        verbose_name = "О Нокатской область"
        verbose_name_plural = "О Нокатской область"
