from django.db import models

from apps.common.models import OrganizationScopedModel


class Product(OrganizationScopedModel):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=120, blank=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("organization", "sku")
        indexes = [models.Index(fields=["organization", "active"])]

    def __str__(self):
        return self.name
