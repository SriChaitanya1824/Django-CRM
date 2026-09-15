from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.text import slugify

from apps.organizations.models import Organization, OrganizationMembership


@transaction.atomic
def register_organization(*, username, email, password, organization_name, first_name="", last_name=""):
    User = get_user_model()
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    base_slug = slugify(organization_name) or username
    slug = base_slug
    i = 2
    while Organization.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{i}"
        i += 1
    organization = Organization.objects.create(name=organization_name, slug=slug)
    OrganizationMembership.objects.create(user=user, organization=organization, role="owner")
    return user, organization
