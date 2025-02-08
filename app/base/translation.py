from modeltranslation.translator import TranslationOptions, register
from app.base.models import We_Invite_To_View, Gallery


@register(We_Invite_To_View)
class We_Invite_To_ViewTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "title_place",
        "description_place",
    )


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ("title_gallery",)
