from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.crud import viewset_for

from .models import Campaign, Segment
from .serializers import CampaignSerializer, SegmentSerializer
from .services import send_campaign


class CampaignViewSet(viewset_for(Campaign, CampaignSerializer, ["name", "subject"])):
    @action(detail=True, methods=["post"])
    def send(self, request, pk=None):
        return Response(CampaignSerializer(send_campaign(campaign=self.get_object(), actor=request.user)).data)


class SegmentViewSet(viewset_for(Segment, SegmentSerializer, ["name", "description"])):
    pass
