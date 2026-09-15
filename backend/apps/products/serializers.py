from apps.common.crud import serializer_for

from .models import Product

ProductSerializer = serializer_for(Product)
