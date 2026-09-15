from django.urls import path

from .views import contacts_export, contacts_import

urlpatterns = [path("contacts/import/", contacts_import), path("contacts/export/", contacts_export)]
