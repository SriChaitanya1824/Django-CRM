from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizationScopedModel(TimeStampedModel):
    organization = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Tag(OrganizationScopedModel):
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=20, default="#2563eb")

    class Meta:
        unique_together = ("organization", "name")
        indexes = [models.Index(fields=["organization", "name"])]

    def __str__(self):
        return self.name


class Activity(OrganizationScopedModel):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    entity_type = models.CharField(max_length=80)
    entity_id = models.PositiveBigIntegerField()
    action = models.CharField(max_length=80)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["organization", "entity_type", "entity_id"])]

