from django.shortcuts import render
from app.base.serializers import We_Invite_To_ViewSerializers, GallerySerializers
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.base.models import We_Invite_To_View, Gallery

# Create your views here.


class We_Invite_To_ViewViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = We_Invite_To_View.objects.all()
    serializer_class = We_Invite_To_ViewSerializers


class GalleryViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
