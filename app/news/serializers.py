from rest_framework import serializers
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "id",
            "title_news",
            "description_news",
            "date_news",
            "image_news",
            "first_paragraph",
            "second_paragraph",
            "general_paragraph",
        ]


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            "id",
            "title_media",
            "description_media",
            "date_media",
            "image_media",
        ]


class NewsNokSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsNok
        fields = [
            "id",
            "title",
            "description",
            "date",
            "photo",
        ]


class TourismNokSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismNok
        fields = [
            "id",
            "title",
            "description",
            "image",
        ]


class AboutNokSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutNok
        fields = [
            "id",
            "description",
            "image",
        ]
