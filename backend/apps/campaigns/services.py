from django.db import transaction

from apps.common.models import Activity


@transaction.atomic
def send_campaign(*, campaign, actor=None):
    contacts = set()
    for segment in campaign.segments.prefetch_related("contacts"):
        contacts.update(segment.contacts.filter(status__in=["new", "active", "customer"]).values_list("id", flat=True))
    campaign.status = "completed"
    campaign.recipients = len(contacts)
    campaign.sent = len(contacts)
    campaign.failed = 0
    campaign.save(update_fields=["status", "recipients", "sent", "failed", "updated_at"])
    Activity.objects.create(organization=campaign.organization, actor=actor, entity_type="campaign", entity_id=campaign.id, action="campaign_completed", metadata={"sent": campaign.sent})
    return campaign
