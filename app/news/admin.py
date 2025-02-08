from django.contrib import admin
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok
from modeltranslation.admin import TranslationAdmin

# Register your models here.


class NewsAdmin(TranslationAdmin):
    fields = ["title_news", "description_news", "date_news", "image_news"]


admin.site.register(News)


class MediaAdmin(TranslationAdmin):
    fields = ["title_media", "description_media", "date_media", "image_media"]


admin.site.register(Media)


class NewsNokAdmin(TranslationAdmin):
    fields = ["title", "description", "date", "photo"]


admin.site.register(NewsNok)


class TourismNokAdmin(TranslationAdmin):
    fields = ["title", "description", "image"]


admin.site.register(TourismNok)


class AboutNokAdmin(TranslationAdmin):
    fields = ["description", "image"]


admin.site.register(AboutNok)
