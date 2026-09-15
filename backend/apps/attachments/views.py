from apps.common.crud import viewset_for

from .models import Attachment
from .serializers import AttachmentSerializer


class AttachmentViewSet(viewset_for(Attachment, AttachmentSerializer, ["original_name", "content_type"])):
    def perform_create(self, serializer):
        uploaded = self.request.FILES.get("file")
        serializer.save(organization=self.get_organization(), uploaded_by=self.request.user, original_name=uploaded.name, size=uploaded.size, content_type=uploaded.content_type)
