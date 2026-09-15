from apps.common.crud import serializer_for

from .models import Contact

ContactSerializer = serializer_for(Contact)
