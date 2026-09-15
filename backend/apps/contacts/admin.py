from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "organization", "company", "status")
    list_filter = ("status", "source")
    search_fields = ("email", "first_name", "last_name")
