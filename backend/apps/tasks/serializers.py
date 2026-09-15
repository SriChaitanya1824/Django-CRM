from apps.common.crud import serializer_for

from .models import Task

TaskSerializer = serializer_for(Task)
