from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "status", "source", "estimated_value", "owner")
    list_filter = ("status", "source", "priority")
    search_fields = ("name", "email", "company")
