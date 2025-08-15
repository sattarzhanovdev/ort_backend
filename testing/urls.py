# app/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet

router = DefaultRouter()
router.register(r"tests", TestViewSet, basename="tests")

urlpatterns = [
    path("", include(router.urls)),
]