from apps.common.crud import serializer_for

from .models import CustomerRequest

CustomerRequestSerializer = serializer_for(CustomerRequest)
