from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.crud import viewset_for

from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewset_for(Notification, NotificationSerializer, ["message", "type"])):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @action(detail=False, methods=["post"])
    def mark_all_read(self, request):
        count = self.get_queryset().filter(read=False).update(read=True)
        return Response({"updated": count})
