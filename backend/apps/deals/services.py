from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction

from apps.common.models import Activity
from apps.common.permissions import active_membership

ALLOWED_STAGE_TRANSITIONS = {
    "qualification": {"discovery", "closed_lost"},
    "discovery": {"proposal", "closed_lost"},
    "proposal": {"negotiation", "closed_lost"},
    "negotiation": {"closed_won", "closed_lost"},
    "closed_won": set(),
    "closed_lost": set(),
}


@transaction.atomic
def advance_deal_stage(*, deal, stage, actor):
    membership = active_membership(actor, deal.organization)
    if not membership or membership.role not in {"owner", "admin", "manager", "sales"}:
        raise PermissionDenied("You cannot move this deal.")
    if stage not in ALLOWED_STAGE_TRANSITIONS[deal.stage]:
        raise ValidationError(f"Cannot move deal from {deal.stage} to {stage}.")
    previous = deal.stage
    deal.stage = stage
    deal.probability = {"discovery": 25, "proposal": 50, "negotiation": 75, "closed_won": 100, "closed_lost": 0}.get(stage, deal.probability)
    deal.save(update_fields=["stage", "probability", "updated_at"])
    Activity.objects.create(organization=deal.organization, actor=actor, entity_type="deal", entity_id=deal.id, action="deal_stage_changed", metadata={"from": previous, "to": stage})
    return deal
