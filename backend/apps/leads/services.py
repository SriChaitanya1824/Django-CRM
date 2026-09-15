from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction

from apps.common.models import Activity
from apps.common.permissions import active_membership
from apps.companies.models import Company
from apps.contacts.models import Contact
from apps.deals.models import Deal

from .models import Lead


@transaction.atomic
def convert_lead(*, lead: Lead, actor, create_company=True, create_deal=True):
    membership = active_membership(actor, lead.organization)
    if not membership or membership.role not in {"owner", "admin", "manager", "sales"}:
        raise PermissionDenied("You cannot convert leads in this organization.")
    if lead.status == "converted":
        raise ValidationError("Lead has already been converted.")
    if lead.status not in {"qualified", "nurturing", "contacted"}:
        raise ValidationError("Lead must be contacted, qualified, or nurturing before conversion.")
    company = None
    if create_company and lead.company:
        company, _ = Company.objects.get_or_create(organization=lead.organization, name=lead.company, defaults={"owner": lead.owner or actor})
    contact = Contact.objects.create(
        organization=lead.organization,
        first_name=lead.name.split(" ")[0],
        last_name=" ".join(lead.name.split(" ")[1:]),
        email=lead.email or f"lead-{lead.id}@example.invalid",
        phone=lead.phone,
        job_title=lead.job_title,
        company=company,
        owner=lead.owner or actor,
        source=lead.source,
    )
    deal = None
    if create_deal:
        deal = Deal.objects.create(
            organization=lead.organization,
            title=f"{lead.name} opportunity",
            company=company,
            contact=contact,
            value=lead.estimated_value,
            owner=lead.owner or actor,
            source=lead.source,
            probability=25,
        )
    lead.status = "converted"
    lead.converted_contact = contact
    lead.converted_deal = deal
    lead.save(update_fields=["status", "converted_contact", "converted_deal", "updated_at"])
    Activity.objects.create(organization=lead.organization, actor=actor, entity_type="lead", entity_id=lead.id, action="lead_converted", metadata={"contact_id": contact.id, "deal_id": getattr(deal, "id", None)})
    return contact, deal
