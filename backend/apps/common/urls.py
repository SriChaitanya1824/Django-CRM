from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, TagViewSet, global_search

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("activities", ActivityViewSet)
urlpatterns = [path("", global_search), *router.urls]
