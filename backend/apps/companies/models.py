from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel, Tag


class Company(OrganizationScopedModel):
    STATUS_CHOICES = [("active", "Active"), ("prospect", "Prospect"), ("customer", "Customer"), ("archived", "Archived")]
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=160, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)
    postal_code = models.CharField(max_length=40, blank=True)
    annual_revenue = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    employee_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="prospect")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        indexes = [models.Index(fields=["organization", "name"]), models.Index(fields=["organization", "status"])]
        unique_together = ("organization", "name")

    def __str__(self):
        return self.name
