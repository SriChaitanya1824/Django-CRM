from django.db import models

from apps.common.models import OrganizationScopedModel


class Segment(OrganizationScopedModel):
    TYPE = [("static", "Static"), ("dynamic", "Dynamic")]
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    filter_definition = models.JSONField(default=dict, blank=True)
    type = models.CharField(max_length=20, choices=TYPE, default="dynamic")
    contacts = models.ManyToManyField("contacts.Contact", blank=True)


class Campaign(OrganizationScopedModel):
    STATUS = [("draft", "Draft"), ("scheduled", "Scheduled"), ("sending", "Sending"), ("completed", "Completed"), ("cancelled", "Cancelled")]
    name = models.CharField(max_length=160)
    subject = models.CharField(max_length=255)
    template = models.ForeignKey("communications.EmailTemplate", null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS, default="draft")
    sender = models.ForeignKey("communications.EmailAccount", null=True, blank=True, on_delete=models.SET_NULL)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    segments = models.ManyToManyField(Segment, blank=True)
    recipients = models.PositiveIntegerField(default=0)
    sent = models.PositiveIntegerField(default=0)
    failed = models.PositiveIntegerField(default=0)
    opened = models.PositiveIntegerField(default=0)
    clicked = models.PositiveIntegerField(default=0)
