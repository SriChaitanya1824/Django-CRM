from apps.common.crud import serializer_for

from .models import Attachment

AttachmentSerializer = serializer_for(Attachment)
