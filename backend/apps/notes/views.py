from apps.common.crud import viewset_for

from .models import Note
from .serializers import NoteSerializer

NoteViewSet = viewset_for(Note, NoteSerializer, ["title", "body"])
