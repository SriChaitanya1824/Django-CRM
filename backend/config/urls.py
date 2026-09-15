from apps.common.views import health, ready
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('ready/', ready),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/v1/auth/', include('apps.accounts.urls')),
    path('api/v1/organizations/', include('apps.organizations.urls')),
    path('api/v1/companies/', include('apps.companies.urls')),
    path('api/v1/contacts/', include('apps.contacts.urls')),
    path('api/v1/leads/', include('apps.leads.urls')),
    path('api/v1/deals/', include('apps.deals.urls')),
    path('api/v1/products/', include('apps.products.urls')),
    path('api/v1/requests/', include('apps.requests.urls')),
    path('api/v1/tasks/', include('apps.tasks.urls')),
    path('api/v1/projects/', include('apps.projects.urls')),
    path('api/v1/notes/', include('apps.notes.urls')),
    path('api/v1/emails/', include('apps.communications.urls')),
    path('api/v1/campaigns/', include('apps.campaigns.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/attachments/', include('apps.attachments.urls')),
    path('api/v1/analytics/', include('apps.analytics.urls')),
    path('api/v1/imports-exports/', include('apps.imports_exports.urls')),
    path('api/v1/search/', include('apps.common.urls')),
]
