from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel


class Notification(OrganizationScopedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    type = models.CharField(max_length=80)
    message = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=80, blank=True)
    entity_id = models.PositiveBigIntegerField(null=True, blank=True)
    read = models.BooleanField(default=False)

    class Meta:
        indexes = [models.Index(fields=["organization", "user", "read"])]
