import pytest
from apps.leads.models import Lead
from apps.leads.services import convert_lead
from apps.organizations.models import Organization, OrganizationMembership
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_convert_lead_creates_contact_and_deal():
    org = Organization.objects.create(name="Alpha", slug="alpha")
    user = get_user_model().objects.create_user(username="owner", email="owner@example.test", password="password123")
    OrganizationMembership.objects.create(user=user, organization=org, role="owner")
    lead = Lead.objects.create(organization=org, name="Avery Stone", email="avery@example.test", company="Example Inc", status="qualified", estimated_value=1000, owner=user)

    contact, deal = convert_lead(lead=lead, actor=user)

    lead.refresh_from_db()
    assert lead.status == "converted"
    assert contact.email == "avery@example.test"
    assert deal.value == 1000


@pytest.mark.django_db
def test_duplicate_lead_conversion_is_rejected():
    org = Organization.objects.create(name="Alpha", slug="alpha")
    user = get_user_model().objects.create_user(username="owner", email="owner@example.test", password="password123")
    OrganizationMembership.objects.create(user=user, organization=org, role="owner")
    lead = Lead.objects.create(organization=org, name="Avery Stone", email="avery@example.test", status="qualified", owner=user)
    convert_lead(lead=lead, actor=user)
    lead.refresh_from_db()

    with pytest.raises(ValidationError):
        convert_lead(lead=lead, actor=user)
