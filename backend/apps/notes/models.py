from django.conf import settings
from django.db import models

from apps.common.models import OrganizationScopedModel


class Note(OrganizationScopedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey("companies.Company", null=True, blank=True, on_delete=models.CASCADE)
    contact = models.ForeignKey("contacts.Contact", null=True, blank=True, on_delete=models.CASCADE)
    lead = models.ForeignKey("leads.Lead", null=True, blank=True, on_delete=models.CASCADE)
    deal = models.ForeignKey("deals.Deal", null=True, blank=True, on_delete=models.CASCADE)
    request = models.ForeignKey("requests.CustomerRequest", null=True, blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey("tasks.Task", null=True, blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
