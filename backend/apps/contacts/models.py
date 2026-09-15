from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel, Tag


class Contact(OrganizationScopedModel):
    STATUS_CHOICES = [("new", "New"), ("active", "Active"), ("customer", "Customer"), ("unsubscribed", "Unsubscribed")]
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    job_title = models.CharField(max_length=160, blank=True)
    company = models.ForeignKey("companies.Company", null=True, blank=True, on_delete=models.SET_NULL, related_name="contacts")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    source = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    notes = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        unique_together = ("organization", "email")
        indexes = [models.Index(fields=["organization", "email"]), models.Index(fields=["organization", "status"])]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email
