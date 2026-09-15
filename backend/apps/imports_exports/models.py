from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel


class DataJob(OrganizationScopedModel):
    TYPE = [("import", "Import"), ("export", "Export")]
    STATUS = [("pending", "Pending"), ("running", "Running"), ("completed", "Completed"), ("failed", "Failed")]
    type = models.CharField(max_length=20, choices=TYPE)
    entity = models.CharField(max_length=40)
    status = models.CharField(max_length=20, choices=STATUS, default="pending")
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    summary = models.JSONField(default=dict, blank=True)
