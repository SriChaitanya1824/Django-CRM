import pytest
from apps.organizations.models import Organization, OrganizationMembership
from apps.tasks.models import Task
from apps.tasks.services import complete_task
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_complete_task_sets_completed_timestamp():
    org = Organization.objects.create(name="Alpha", slug="alpha")
    user = get_user_model().objects.create_user(username="manager", email="manager@example.test", password="password123")
    OrganizationMembership.objects.create(user=user, organization=org, role="manager")
    task = Task.objects.create(organization=org, title="Call customer", created_by=user, assigned_to=user)
    complete_task(task=task, actor=user)
    task.refresh_from_db()
    assert task.status == "done"
    assert task.completed_at is not None
