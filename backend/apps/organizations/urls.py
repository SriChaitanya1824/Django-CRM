from rest_framework.routers import DefaultRouter

from .views import MembershipViewSet, OrganizationViewSet

router = DefaultRouter()
router.register("memberships", MembershipViewSet, basename="membership")
router.register("", OrganizationViewSet, basename="organization")
urlpatterns = router.urls
