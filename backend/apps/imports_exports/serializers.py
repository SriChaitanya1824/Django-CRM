from apps.common.crud import serializer_for

from .models import DataJob

DataJobSerializer = serializer_for(DataJob)
