from rest_framework import serializers
from app.base.models import We_Invite_To_View, Gallery


class We_Invite_To_ViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = We_Invite_To_View
        fields = [
            "title",
            "title_place",
            "description_place",
            "date_place",
            "image_place",
        ]


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["title_gallery", "photo"]
