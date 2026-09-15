from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel, Tag


class Task(OrganizationScopedModel):
    STATUS_CHOICES = [("todo", "Todo"), ("in_progress", "In Progress"), ("blocked", "Blocked"), ("done", "Done")]
    PRIORITY_CHOICES = [("low", "Low"), ("medium", "Medium"), ("high", "High"), ("urgent", "Urgent")]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_tasks")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="created_tasks")
    company = models.ForeignKey("companies.Company", null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey("contacts.Contact", null=True, blank=True, on_delete=models.SET_NULL)
    lead = models.ForeignKey("leads.Lead", null=True, blank=True, on_delete=models.SET_NULL)
    deal = models.ForeignKey("deals.Deal", null=True, blank=True, on_delete=models.SET_NULL)
    request = models.ForeignKey("requests.CustomerRequest", null=True, blank=True, on_delete=models.SET_NULL)
    project = models.ForeignKey("projects.Project", null=True, blank=True, on_delete=models.SET_NULL, related_name="tasks")
    parent_task = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="subtasks")
    completed_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
