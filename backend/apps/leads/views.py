from django.core.exceptions import PermissionDenied, ValidationError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.crud import viewset_for

from .models import Lead
from .serializers import LeadSerializer
from .services import convert_lead


class LeadViewSet(viewset_for(Lead, LeadSerializer, ["name", "email", "company", "source"])):
    @action(detail=True, methods=["post"])
    def convert(self, request, pk=None):
        try:
            contact, deal = convert_lead(lead=self.get_object(), actor=request.user)
        except (ValidationError, PermissionDenied) as exc:
            return Response({"success": False, "error": {"code": "INVALID_CONVERSION", "message": str(exc), "details": {}}}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": True, "contact_id": contact.id, "deal_id": getattr(deal, "id", None)})
