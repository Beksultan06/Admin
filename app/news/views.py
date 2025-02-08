from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok
from app.news.serializers import (
    NewsSerializer,
    MediaSerializer,
    NewsNokSerializer,
    AboutNokSerializer,
    TourismNokSerializer,
)

# Create your views here.


class NewsAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class MediaAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class NewsNokAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsNokSerializer


class TourismNokAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = TourismNok.objects.all()
    serializer_class = TourismNokSerializer


class AboutNokAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = AboutNok.objects.all()
    serializer_class = AboutNokSerializer
