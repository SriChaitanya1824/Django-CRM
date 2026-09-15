from apps.common.crud import viewset_for

from .models import Contact
from .serializers import ContactSerializer

ContactViewSet = viewset_for(Contact, ContactSerializer, ["first_name", "last_name", "email", "phone", "job_title"])
