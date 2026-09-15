from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("action", "organization", "user", "entity_type", "timestamp")
    list_filter = ("action", "timestamp")
    search_fields = ("action", "entity_type", "entity_id")
    readonly_fields = ("timestamp",)
