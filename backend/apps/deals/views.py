from django.core.exceptions import PermissionDenied, ValidationError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.crud import viewset_for

from .models import Deal
from .serializers import DealSerializer
from .services import advance_deal_stage


class DealViewSet(viewset_for(Deal, DealSerializer, ["title", "pipeline", "source"])):
    @action(detail=True, methods=["post"])
    def advance(self, request, pk=None):
        try:
            deal = advance_deal_stage(deal=self.get_object(), stage=request.data.get("stage"), actor=request.user)
        except (ValidationError, PermissionDenied) as exc:
            return Response({"success": False, "error": {"code": "INVALID_STAGE", "message": str(exc), "details": {}}}, status=status.HTTP_400_BAD_REQUEST)
        return Response(DealSerializer(deal).data)
