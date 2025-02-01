from django.urls import path
from rest_framework.routers import DefaultRouter
from app.base.views import We_Invite_To_ViewViewSet, GalleryViewSet

router = DefaultRouter()
router.register(r'we-invite-to-view', We_Invite_To_ViewViewSet, basename="we-invite-to-view")
router.register(r'gallery', GalleryViewSet, basename="gallery")

urlpatterns = [
    
]

urlpatterns += router.urls