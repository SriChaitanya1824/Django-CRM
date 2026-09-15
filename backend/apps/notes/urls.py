from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

router = DefaultRouter()
router.register("", NoteViewSet)
urlpatterns = router.urls
