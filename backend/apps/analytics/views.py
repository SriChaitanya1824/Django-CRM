from django.db.models import Count, DecimalField, ExpressionWrapper, F, Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.deals.models import Deal
from apps.leads.models import Lead
from apps.requests.models import CustomerRequest
from apps.tasks.models import Task


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):
    org = request.user.memberships.filter(status="active").first().organization
    weighted = ExpressionWrapper(F("value") * F("probability") / 100, output_field=DecimalField())
    return Response({
        "total_leads": Lead.objects.filter(organization=org).count(),
        "open_deals": Deal.objects.filter(organization=org).exclude(stage__in=["closed_won", "closed_lost"]).count(),
        "won_deals": Deal.objects.filter(organization=org, stage="closed_won").count(),
        "lost_deals": Deal.objects.filter(organization=org, stage="closed_lost").count(),
        "pipeline_value": Deal.objects.filter(organization=org).aggregate(v=Sum("value"))["v"] or 0,
        "forecast_revenue": Deal.objects.filter(organization=org).aggregate(v=Sum(weighted))["v"] or 0,
        "pending_tasks": Task.objects.filter(organization=org).exclude(status="done").count(),
        "open_requests": CustomerRequest.objects.filter(organization=org).exclude(status__in=["resolved", "closed"]).count(),
        "leads_by_source": list(Lead.objects.filter(organization=org).values("source").annotate(count=Count("id"))),
        "deals_by_stage": list(Deal.objects.filter(organization=org).values("stage").annotate(value=Sum("value"), count=Count("id"))),
        "tasks_by_status": list(Task.objects.filter(organization=org).values("status").annotate(count=Count("id"))),
        "requests_by_status": list(CustomerRequest.objects.filter(organization=org).values("status").annotate(count=Count("id"))),
    })
