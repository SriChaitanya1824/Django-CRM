from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from apps.common.models import OrganizationScopedModel


def validate_attachment(file):
    allowed = {".pdf", ".png", ".jpg", ".jpeg", ".csv", ".txt", ".docx", ".xlsx"}
    if Path(file.name).suffix.lower() not in allowed:
        raise ValidationError("Unsupported file type.")
    if file.size > 10 * 1024 * 1024:
        raise ValidationError("Attachment exceeds 10MB.")


class Attachment(OrganizationScopedModel):
    file = models.FileField(upload_to="attachments/%Y/%m/", validators=[validate_attachment])
    original_name = models.CharField(max_length=255)
    size = models.PositiveBigIntegerField()
    content_type = models.CharField(max_length=120)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    entity_type = models.CharField(max_length=80, blank=True)
    entity_id = models.PositiveBigIntegerField(null=True, blank=True)
