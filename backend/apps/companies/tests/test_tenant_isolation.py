import pytest
from apps.companies.models import Company
from apps.organizations.models import Organization, OrganizationMembership
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_company_list_is_limited_to_active_membership(settings):
    org_a = Organization.objects.create(name="Alpha", slug="alpha")
    org_b = Organization.objects.create(name="Beta", slug="beta")
    user = get_user_model().objects.create_user(username="agent", email="agent@example.test", password="password123")
    OrganizationMembership.objects.create(user=user, organization=org_a, role="sales")
    Company.objects.create(organization=org_a, name="Visible Co")
    Company.objects.create(organization=org_b, name="Hidden Co")

    client = APIClient()
    client.force_authenticate(user)
    response = client.get("/api/v1/companies/", HTTP_X_ORGANIZATION_ID=str(org_a.id))

    assert response.status_code == 200
    names = [item["name"] for item in response.data["results"]]
    assert names == ["Visible Co"]
