from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "status", "owner", "updated_at")
    list_filter = ("status", "industry", "country")
    search_fields = ("name", "email", "website")
