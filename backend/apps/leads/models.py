from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel, Tag


class Lead(OrganizationScopedModel):
    STATUS_CHOICES = [("new", "New"), ("contacted", "Contacted"), ("qualified", "Qualified"), ("nurturing", "Nurturing"), ("converted", "Converted"), ("lost", "Lost")]
    SOURCE_CHOICES = [("website", "Website"), ("referral", "Referral"), ("advertisement", "Advertisement"), ("social", "Social Media"), ("cold", "Cold Outreach"), ("event", "Event"), ("import", "Import"), ("other", "Other")]
    PRIORITY_CHOICES = [("low", "Low"), ("medium", "Medium"), ("high", "High"), ("urgent", "Urgent")]
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=160, blank=True)
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES, default="website")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="new")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    estimated_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_team = models.CharField(max_length=120, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField(blank=True)
    converted_contact = models.ForeignKey("contacts.Contact", null=True, blank=True, on_delete=models.SET_NULL)
    converted_deal = models.ForeignKey("deals.Deal", null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        indexes = [models.Index(fields=["organization", "status"]), models.Index(fields=["organization", "source"])]

    def __str__(self):
        return self.name
