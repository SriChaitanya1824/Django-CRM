from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel


class Project(OrganizationScopedModel):
    STATUS_CHOICES = [("planned", "Planned"), ("active", "Active"), ("on_hold", "On Hold"), ("completed", "Completed"), ("archived", "Archived")]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="crm_projects")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="planned")
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    @property
    def progress(self):
        total = self.tasks.count()
        return 0 if total == 0 else round(self.tasks.filter(status="done").count() / total * 100)

    def __str__(self):
        return self.name
