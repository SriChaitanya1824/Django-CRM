from django.contrib import admin

from .models import Activity, Tag

admin.site.register(Tag)
admin.site.register(Activity)
