from apps.common.crud import serializer_for

from .models import Company

CompanySerializer = serializer_for(Company)
