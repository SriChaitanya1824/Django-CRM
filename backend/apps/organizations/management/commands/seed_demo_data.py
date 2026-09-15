from apps.accounts.services import register_organization
from apps.common.models import Activity, Tag
from apps.companies.models import Company
from apps.contacts.models import Contact
from apps.deals.models import Deal
from apps.leads.models import Lead
from apps.notifications.models import Notification
from apps.products.models import Product
from apps.projects.models import Project
from apps.requests.models import CustomerRequest
from apps.tasks.models import Task
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed fictional PulseCRM demo data."

    def handle(self, *args, **options):
        for org_name, username in [("Northstar Studio", "owner"), ("Cedar Cloud", "cedarowner")]:
            user, org = register_organization(username=username, email=f"{username}@pulsecrm.test", password="DemoPass123!", organization_name=org_name)
            tag = Tag.objects.create(organization=org, name="Strategic", color="#0f766e")
            company = Company.objects.create(organization=org, name=f"{org_name} Labs", industry="Software", email="hello@example.test", owner=user, status="customer")
            company.tags.add(tag)
            contact = Contact.objects.create(organization=org, first_name="Avery", last_name="Stone", email=f"avery.{username}@example.test", company=company, owner=user, source="referral")
            Lead.objects.create(organization=org, name="Jordan Lee", email=f"jordan.{username}@example.test", company="Bright Path", status="qualified", source="website", estimated_value=42000, owner=user)
            deal = Deal.objects.create(organization=org, title="Expansion package", company=company, contact=contact, value=86000, probability=50, stage="proposal", owner=user)
            Product.objects.create(organization=org, name="PulseCRM Growth Seat", sku=f"GROW-{org.id}", unit_price=79)
            request = CustomerRequest.objects.create(organization=org, title="Billing workflow question", description="Customer needs help with invoice routing.", company=company, contact=contact, assigned_to=user)
            project = Project.objects.create(organization=org, name="Customer onboarding", owner=user, status="active")
            Task.objects.create(organization=org, title="Schedule kickoff", company=company, contact=contact, deal=deal, request=request, project=project, assigned_to=user, created_by=user)
            Activity.objects.create(organization=org, actor=user, entity_type="company", entity_id=company.id, action="created")
            Notification.objects.create(organization=org, user=user, type="deadline_approaching", message="Kickoff task is due soon", entity_type="task", entity_id=1)
        self.stdout.write(self.style.SUCCESS("Demo data created. Login: owner / DemoPass123!"))
