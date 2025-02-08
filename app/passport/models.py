from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Passport(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Заголовок для "Паспорт района"'
    )
    image = models.ImageField(
        upload_to="passport_images/", verbose_name='Фото для "Паспорт района"'
    )
    description = RichTextField(verbose_name='Описание для "Паспорт района"')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Паспорт района"
        verbose_name_plural = "Паспорта районов"


class GeneralInformation(models.Model):
    title = models.CharField(max_length=135, verbose_name="Заголовок")
    description = RichTextField(verbose_name="Описание Общей Информации")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")

    def str(self):
        return self.title

    class Meta:
        verbose_name = "Общая Информация"
        verbose_name_plural = "Общая Информация"


class Info(models.Model):
    title = models.TextField(verbose_name="Заголовок")
    image = models.ImageField(upload_to="op/")
    description = RichTextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Айылных маймаков"
        verbose_name_plural = "Айылных маймаков"


# ВЛР-Выдвющиеся личности района
class HeadPersonality(models.Model):
    title_personality = models.CharField(
        max_length=100,
        verbose_name="Заголовок ВЛР ",
    )
    image_personality = models.ImageField(
        upload_to="personalities/",
        verbose_name="Изображение ВЛР",
    )

    def __str__(self):
        return self.title_personality

    class Meta:
        verbose_name = "Выдвющиеся личности района"
        verbose_name_plural = "Выдвющиеся личности района"


class Personality(models.Model):
    name_person = models.CharField(
        max_length=100,
        verbose_name="Имя личности",
    )
    description_person = models.TextField(
        verbose_name="Описание личности",
    )
    image_person = models.ImageField(
        upload_to="personalities/",
        verbose_name="Изображение личности",
    )
    all_description_person = RichTextField(
        verbose_name="Полное описание личности",
    )

    def __str__(self):
        return "Личности района: " + self.name_person

    class Meta:
        verbose_name = "Личность"
        verbose_name_plural = "Личности"


class History(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Заголовок для "История района"'
    )
    image = models.ImageField(
        upload_to="history_images/", verbose_name='Фото для "История айона"'
    )
    description = RichTextField(verbose_name='Описание для "История района"')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "История района"
        verbose_name_plural = "История районов"


# моделька для карта района
class Map(models.Model):
    title = models.TextField(verbose_name="Заголовок")
    image = models.ImageField(upload_to="locations/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Карта района"


class Vacancy(models.Model):
    title = models.TextField(verbose_name="Заголовок вакансии")
    description = RichTextField(verbose_name="Описание вакансий")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Вакансия"
