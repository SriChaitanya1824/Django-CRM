from apps.common.crud import viewset_for

from .models import Company
from .serializers import CompanySerializer

CompanyViewSet = viewset_for(Company, CompanySerializer, ["name", "email", "industry", "city", "country"])
