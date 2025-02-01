from rest_framework import serializers
from .models import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins 
from rest_framework import serializers
from app.passport.models import HeadPersonality, Personality

class GalleryOshTourSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryOshTour
        fields = ['id', 'title', 'image']

class GalleryArchivalPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryArchivalPhotos
        fields = ['id', 'image']

class GalleryNewShapesSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryNewShapes
        fields = ['id', 'image']
