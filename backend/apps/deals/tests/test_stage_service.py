import pytest
from apps.deals.models import Deal
from apps.deals.services import advance_deal_stage
from apps.organizations.models import Organization, OrganizationMembership
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_deal_stage_transition_is_validated():
    org = Organization.objects.create(name="Alpha", slug="alpha")
    user = get_user_model().objects.create_user(username="sales", email="sales@example.test", password="password123")
    OrganizationMembership.objects.create(user=user, organization=org, role="sales")
    deal = Deal.objects.create(organization=org, title="Expansion", value=5000, stage="qualification")
    advance_deal_stage(deal=deal, stage="discovery", actor=user)
    deal.refresh_from_db()
    assert deal.stage == "discovery"
    with pytest.raises(ValidationError):
        advance_deal_stage(deal=deal, stage="closed_won", actor=user)
