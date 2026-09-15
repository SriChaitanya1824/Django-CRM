from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel


class EmailAccount(OrganizationScopedModel):
    name = models.CharField(max_length=120)
    email_address = models.EmailField()
    provider = models.CharField(max_length=80, default="smtp")
    smtp_host = models.CharField(max_length=160, blank=True)
    smtp_port = models.PositiveIntegerField(default=587)
    username = models.CharField(max_length=160, blank=True)
    encrypted_credentials = models.TextField(blank=True)
    imap_host = models.CharField(max_length=160, blank=True)
    imap_port = models.PositiveIntegerField(default=993)
    enabled = models.BooleanField(default=True)
    sync_enabled = models.BooleanField(default=False)


class EmailTemplate(OrganizationScopedModel):
    name = models.CharField(max_length=160)
    subject = models.CharField(max_length=255)
    body = models.TextField()


class EmailSignature(OrganizationScopedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    body = models.TextField()


class EmailMessage(OrganizationScopedModel):
    DIRECTION = [("inbound", "Inbound"), ("outbound", "Outbound")]
    STATUS = [("draft", "Draft"), ("queued", "Queued"), ("sent", "Sent"), ("failed", "Failed"), ("received", "Received")]
    sender = models.EmailField()
    recipients = models.JSONField(default=list)
    cc = models.JSONField(default=list, blank=True)
    bcc = models.JSONField(default=list, blank=True)
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    html_body = models.TextField(blank=True)
    direction = models.CharField(max_length=20, choices=DIRECTION, default="outbound")
    status = models.CharField(max_length=20, choices=STATUS, default="draft")
    sent_at = models.DateTimeField(null=True, blank=True)
    received_at = models.DateTimeField(null=True, blank=True)
    contact = models.ForeignKey("contacts.Contact", null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey("companies.Company", null=True, blank=True, on_delete=models.SET_NULL)
    lead = models.ForeignKey("leads.Lead", null=True, blank=True, on_delete=models.SET_NULL)
    deal = models.ForeignKey("deals.Deal", null=True, blank=True, on_delete=models.SET_NULL)
    request = models.ForeignKey("requests.CustomerRequest", null=True, blank=True, on_delete=models.SET_NULL)
