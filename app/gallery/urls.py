from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryOshTourViewSet, GalleryArchivalPhotosViewSet, GalleryNewShapesViewSet

router = DefaultRouter()
router.register(r'GalleryNewShapes', GalleryNewShapesViewSet, basename='GalleryNewShapes')
router.register(r'GalleryOshTour', GalleryOshTourViewSet, basename='GalleryOshTour',)
router.register(r'GalleryArchivalPhotos', GalleryArchivalPhotosViewSet, basename='GalleryArchivalPhotos',)

urlpatterns = [
    path('', include(router.urls)),
]