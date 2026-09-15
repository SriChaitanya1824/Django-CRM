from apps.common.crud import serializer_for

from .models import Note

NoteSerializer = serializer_for(Note)
