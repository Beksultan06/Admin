from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.news.views import NewsAPI, MediaAPI, NewsNokAPI, AboutNokAPI, TourismNokAPI

router = DefaultRouter()
router.register(r"news", NewsAPI, basename="news")
router.register(r"media", MediaAPI, basename="media")
router.register(r"news-nok", NewsNokAPI, basename="news_nok")
router.register(r"tourism-nok", TourismNokAPI, basename="tourism_nok")
router.register(r"about-nok", AboutNokAPI, basename="about_nok")


urlpatterns = [
    path("", include(router.urls)),
]
