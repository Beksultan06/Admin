# Generated by Django 4.2 on 2025-02-01 10:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_aboutnok_newsnok_tourismnok"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutnok",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="aboutnok",
            name="description_ky",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="aboutnok",
            name="description_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="media",
            name="description_media",
            field=ckeditor.fields.RichTextField(
                verbose_name='Описание СМИ страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="media",
            name="description_media_ky",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name='Описание СМИ страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="media",
            name="description_media_ru",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name='Описание СМИ страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_news",
            field=ckeditor.fields.RichTextField(
                verbose_name='Описание новостей страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_news_ky",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name='Описание новостей страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="description_news_ru",
            field=ckeditor.fields.RichTextField(
                null=True, verbose_name='Описание новостей страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="first_paragraph",
            field=ckeditor.fields.RichTextField(
                verbose_name='Первый абзац детальный просмотр новостей страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="first_paragraph_ky",
            field=ckeditor.fields.RichTextField(
                null=True,
                verbose_name='Первый абзац детальный просмотр новостей страницы "Новости"',
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="first_paragraph_ru",
            field=ckeditor.fields.RichTextField(
                null=True,
                verbose_name='Первый абзац детальный просмотр новостей страницы "Новости"',
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="second_paragraph",
            field=ckeditor.fields.RichTextField(
                verbose_name='Второй абзац детальный просмотр новостей страницы "Новости"'
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="second_paragraph_ky",
            field=ckeditor.fields.RichTextField(
                null=True,
                verbose_name='Второй абзац детальный просмотр новостей страницы "Новости"',
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="second_paragraph_ru",
            field=ckeditor.fields.RichTextField(
                null=True,
                verbose_name='Второй абзац детальный просмотр новостей страницы "Новости"',
            ),
        ),
        migrations.AlterField(
            model_name="newsnok",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="newsnok",
            name="description_ky",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="newsnok",
            name="description_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="newsnok",
            name="title",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="newsnok",
            name="title_ky",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="newsnok",
            name="title_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="tourismnok",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="tourismnok",
            name="description_ky",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="tourismnok",
            name="description_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="tourismnok",
            name="title",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="tourismnok",
            name="title_ky",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name="tourismnok",
            name="title_ru",
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
