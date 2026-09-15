from rest_framework.routers import DefaultRouter

from .views import CampaignViewSet, SegmentViewSet

router = DefaultRouter()
router.register("segments", SegmentViewSet)
router.register("", CampaignViewSet)
urlpatterns = router.urls
