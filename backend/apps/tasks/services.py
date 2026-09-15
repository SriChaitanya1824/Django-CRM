from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction
from django.utils import timezone

from apps.common.models import Activity
from apps.common.permissions import active_membership
from apps.notifications.models import Notification


@transaction.atomic
def complete_task(*, task, actor):
    membership = active_membership(actor, task.organization)
    if not membership or membership.role == "viewer":
        raise PermissionDenied("You cannot complete this task.")
    if task.status == "done":
        raise ValidationError("Task is already complete.")
    task.status = "done"
    task.completed_at = timezone.now()
    task.save(update_fields=["status", "completed_at", "updated_at"])
    Activity.objects.create(organization=task.organization, actor=actor, entity_type="task", entity_id=task.id, action="task_completed")
    if task.assigned_to and task.assigned_to != actor:
        Notification.objects.create(organization=task.organization, user=task.assigned_to, type="task_completed", message=f"{task.title} was completed", entity_type="task", entity_id=task.id)
    return task


def assign_record(*, record, user, actor):
    membership = active_membership(actor, record.organization)
    if not membership or membership.role not in {"owner", "admin", "manager"}:
        raise PermissionDenied("You cannot assign records.")
    record.owner = user if hasattr(record, "owner") else getattr(record, "assigned_to", user)
    record.save()
    return record


def create_reminder(*, organization, user, message, entity_type="", entity_id=None):
    return Notification.objects.create(organization=organization, user=user, type="reminder", message=message, entity_type=entity_type, entity_id=entity_id)
