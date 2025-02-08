from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .translation import *
from .models import *


class GalleryNewShapesAdmin(TranslationAdmin):
    fieldsets = (
        (
            "Изображения",
            {
                "fields": ["image"],
            },
        ),
    )


admin.site.register(GalleryNewShapes, GalleryNewShapesAdmin)


class GalleryOshTourAdmin(TranslationAdmin):
    fieldsets = (
        (
            "Изображения",
            {
                "fields": ["image"],
            },
        ),
        (
            "Русская версия",
            {
                "fields": ["title_ru"],
            },
        ),
        (
            "Кыргызская версия",
            {
                "fields": ["title_ky"],
            },
        ),
    )


admin.site.register(GalleryOshTour, GalleryOshTourAdmin)


class GalleryArchivalPhotosAdmin(TranslationAdmin):
    fieldsets = (
        (
            "Изображения",
            {
                "fields": ["image"],
            },
        ),
    )


admin.site.register(GalleryArchivalPhotos, GalleryArchivalPhotosAdmin)
