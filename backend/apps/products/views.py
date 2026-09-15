from apps.common.crud import viewset_for

from .models import Product
from .serializers import ProductSerializer

ProductViewSet = viewset_for(Product, ProductSerializer, ["name", "sku", "category"])
