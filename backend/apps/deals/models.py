from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.common.models import OrganizationScopedModel, Tag


class Deal(OrganizationScopedModel):
    STAGES = [("qualification", "Qualification"), ("discovery", "Discovery"), ("proposal", "Proposal"), ("negotiation", "Negotiation"), ("closed_won", "Closed Won"), ("closed_lost", "Closed Lost")]
    title = models.CharField(max_length=255)
    company = models.ForeignKey("companies.Company", null=True, blank=True, on_delete=models.SET_NULL, related_name="deals")
    contact = models.ForeignKey("contacts.Contact", null=True, blank=True, on_delete=models.SET_NULL, related_name="deals")
    value = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    currency = models.CharField(max_length=8, default="USD")
    probability = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])
    expected_close_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    pipeline = models.CharField(max_length=80, default="Default")
    stage = models.CharField(max_length=30, choices=STAGES, default="qualification")
    source = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    @property
    def weighted_pipeline_value(self):
        return self.value * self.probability / 100

    class Meta:
        indexes = [models.Index(fields=["organization", "stage"]), models.Index(fields=["organization", "expected_close_date"])]

    def __str__(self):
        return self.title
