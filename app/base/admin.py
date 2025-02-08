from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import We_Invite_To_View, Gallery

# Register your models here.


class We_Invite_To_ViewAdmin(TranslationAdmin):
    fields = ("title", "title_place", "description_place", "date_place", "image_place")


class GalleryAdmin(TranslationAdmin):
    fields = ("title_gallery", "photo")


admin.site.register(We_Invite_To_View)
admin.site.register(Gallery)
