from rest_framework.routers import DefaultRouter

from .views import CustomerRequestViewSet

router = DefaultRouter()
router.register("", CustomerRequestViewSet)
urlpatterns = router.urls
