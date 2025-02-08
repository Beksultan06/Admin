from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .translation import *
from .models import *


class PassportAdmin(TranslationAdmin):
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
                "fields": ["title_ru", "description_ru"],
            },
        ),
        (
            "Кыргызская версия",
            {
                "fields": ["title_ky", "description_ky"],
            },
        ),
    )


admin.site.register(Passport, PassportAdmin)


class GeneralInformationAdmin(TranslationAdmin):
    fields = ["title", "description", "image"]


admin.site.register(GeneralInformation, GeneralInformationAdmin)


class InfoAdmin(TranslationAdmin):
    fields = ["title", "image", "description"]


admin.site.register(Info, InfoAdmin)


class HeadPersonalityAdmin(TranslationAdmin):
    fieldsets = (
        (
            "Изображение",
            {
                "fields": [
                    "image_personality",
                ],
            },
        ),
        (
            "Русская версия",
            {
                "fields": [
                    "title_personality_ru",
                ],
            },
        ),
        (
            "Кыргызская версия",
            {
                "fields": [
                    "title_personality_ky",
                ],
            },
        ),
    )


admin.site.register(HeadPersonality, HeadPersonalityAdmin)


class PersonalityAdmin(TranslationAdmin):
    fieldsets = (
        (
            "Изображение",
            {
                "fields": [
                    "image_person",
                ],
            },
        ),
        (
            "Русская версия",
            {
                "fields": [
                    "name_person_ru",
                    "description_person_ru",
                    "all_description_person_ru",
                ],
            },
        ),
        (
            "Кыргызская версия",
            {
                "fields": [
                    "name_person_ky",
                    "description_person_ky",
                    "all_description_person_ky",
                ],
            },
        ),
    )


admin.site.register(Personality, PersonalityAdmin)


class HistoryAdmin(TranslationAdmin):
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
                "fields": ["title_ru", "description_ru"],
            },
        ),
        (
            "Кыргызская версия",
            {
                "fields": ["title_ky", "description_ky"],
            },
        ),
    )


admin.site.register(History, HistoryAdmin)

admin.site.register(Map)


class VacancyAdmin(TranslationAdmin):
    fieleds = ["title", "description"]


admin.site.register(Vacancy, VacancyAdmin)
