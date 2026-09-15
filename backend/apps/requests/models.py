from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel, Tag


class CustomerRequest(OrganizationScopedModel):
    STATUS_CHOICES = [("open", "Open"), ("in_progress", "In Progress"), ("waiting", "Waiting"), ("resolved", "Resolved"), ("closed", "Closed")]
    PRIORITY_CHOICES = [("low", "Low"), ("medium", "Medium"), ("high", "High"), ("urgent", "Urgent")]
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey("companies.Company", null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey("contacts.Contact", null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="open")
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=120, blank=True)
    source = models.CharField(max_length=80, default="email")
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
