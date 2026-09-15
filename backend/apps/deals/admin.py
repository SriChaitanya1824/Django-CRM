from django.contrib import admin

from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "stage", "value", "probability", "owner")
    list_filter = ("stage", "pipeline")
    search_fields = ("title",)
