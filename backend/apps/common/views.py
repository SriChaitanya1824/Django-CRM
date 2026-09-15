from django.db import connection
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.companies.models import Company
from apps.contacts.models import Contact
from apps.deals.models import Deal
from apps.leads.models import Lead
from apps.projects.models import Project
from apps.requests.models import CustomerRequest
from apps.tasks.models import Task

from .models import Activity, Tag
from .serializers import ActivitySerializer, TagSerializer


def health(_request):
    return JsonResponse({"status": "ok"})


def ready(_request):
    with connection.cursor() as cursor:
        cursor.execute("select 1")
    return JsonResponse({"status": "ready"})


class TenantViewSet(viewsets.ModelViewSet):
    organization_kwarg = "organization"

    def get_organization(self):
        org_id = self.request.headers.get("X-Organization-ID") or self.request.query_params.get("organization")
        memberships = self.request.user.memberships.filter(status="active")
        return memberships.filter(organization_id=org_id).first().organization if org_id else memberships.first().organization

    def get_queryset(self):
        org = self.get_organization()
        qs = super().get_queryset()
        return qs.filter(organization=org).order_by("-updated_at", "-id") if org else qs.none()

    def perform_create(self, serializer):
        serializer.save(organization=self.get_organization())


class TagViewSet(TenantViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    search_fields = ["name"]


class ActivityViewSet(TenantViewSet):
    queryset = Activity.objects.select_related("actor", "organization")
    serializer_class = ActivitySerializer


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def global_search(request):
    org = request.user.memberships.filter(status="active").first().organization
    term = request.query_params.get("q", "")
    results = []
    models = [(Company, "company", "name"), (Contact, "contact", "email"), (Lead, "lead", "name"), (Deal, "deal", "title"), (CustomerRequest, "request", "title"), (Task, "task", "title"), (Project, "project", "name")]
    for model, kind, field in models:
        for obj in model.objects.filter(organization=org, **{f"{field}__icontains": term})[:8]:
            results.append({"type": kind, "id": obj.id, "label": str(obj)})
    return Response({"results": results})
