from apps.common.crud import serializer_for

from .models import Notification

NotificationSerializer = serializer_for(Notification)
