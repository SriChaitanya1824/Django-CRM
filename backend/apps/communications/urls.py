from rest_framework.routers import DefaultRouter

from .views import EmailAccountViewSet, EmailMessageViewSet, EmailSignatureViewSet, EmailTemplateViewSet

router = DefaultRouter()
router.register("accounts", EmailAccountViewSet)
router.register("messages", EmailMessageViewSet)
router.register("templates", EmailTemplateViewSet)
router.register("signatures", EmailSignatureViewSet)
urlpatterns = router.urls
