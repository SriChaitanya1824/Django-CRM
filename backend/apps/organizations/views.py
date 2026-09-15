from rest_framework import viewsets

from apps.common.views import TenantViewSet

from .models import Organization, OrganizationMembership
from .serializers import OrganizationMembershipSerializer, OrganizationSerializer


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    def get_queryset(self):
        return Organization.objects.filter(members__user=self.request.user, members__status="active").distinct()


class MembershipViewSet(TenantViewSet):
    queryset = OrganizationMembership.objects.select_related("user", "organization")
    serializer_class = OrganizationMembershipSerializer
    def get_queryset(self):
        org = self.get_organization()
        return self.queryset.filter(organization=org) if org else self.queryset.none()
