from apps.common.crud import serializer_for

from .models import Campaign, Segment

CampaignSerializer = serializer_for(Campaign)
SegmentSerializer = serializer_for(Segment)
