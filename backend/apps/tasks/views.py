from django.core.exceptions import PermissionDenied, ValidationError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.crud import viewset_for

from .models import Task
from .serializers import TaskSerializer
from .services import complete_task


class TaskViewSet(viewset_for(Task, TaskSerializer, ["title", "description"])):
    def perform_create(self, serializer):
        serializer.save(organization=self.get_organization(), created_by=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        try:
            task = complete_task(task=self.get_object(), actor=request.user)
        except (ValidationError, PermissionDenied) as exc:
            return Response({"success": False, "error": {"code": "INVALID_TASK_STATE", "message": str(exc), "details": {}}}, status=status.HTTP_400_BAD_REQUEST)
        return Response(TaskSerializer(task).data)
