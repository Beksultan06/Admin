from modeltranslation.translator import register, TranslationOptions
from .models import GalleryNewShapes, GalleryOshTour, GalleryArchivalPhotos


@register(GalleryNewShapes)
class GalleryNewShapesTranslationOptions(TranslationOptions):
    fields = ("image",)


@register(GalleryOshTour)
class GalleryOshTourTranslationOptions(TranslationOptions):
    fields = ("title", "image")


@register(GalleryArchivalPhotos)
class GalleryArchivalPhotosTranslationOptions(TranslationOptions):
    fields = ("image",)
