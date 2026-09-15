from rest_framework.permissions import SAFE_METHODS, BasePermission

from apps.organizations.models import OrganizationMembership


def active_membership(user, organization):
    if not user or not user.is_authenticated or organization is None:
        return None
    return OrganizationMembership.objects.filter(
        user=user, organization=organization, status="active"
    ).first()


class IsOrganizationMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        org = getattr(obj, "organization", obj)
        membership = active_membership(request.user, org)
        if request.method in SAFE_METHODS:
            return membership is not None
        return membership is not None and membership.role != "viewer"

