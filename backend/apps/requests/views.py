from apps.common.crud import viewset_for

from .models import CustomerRequest
from .serializers import CustomerRequestSerializer

CustomerRequestViewSet = viewset_for(CustomerRequest, CustomerRequestSerializer, ["title", "description", "category"])
