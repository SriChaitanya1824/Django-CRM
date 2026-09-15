from apps.common.crud import serializer_for

from .models import Lead

LeadSerializer = serializer_for(Lead)
