from rest_framework import serializers

from .views import TenantViewSet


def serializer_for(model):
    class AutoSerializer(serializers.ModelSerializer):
        class Meta:
            fields = "__all__"
            read_only_fields = ("organization", "created_at", "updated_at")

    AutoSerializer.Meta.model = model
    AutoSerializer.__name__ = f"{model.__name__}Serializer"
    return AutoSerializer


def viewset_for(model, serializer=None, search_fields=None, ordering_fields=None):
    resolved_search_fields = search_fields or []
    resolved_ordering_fields = ordering_fields or ["created_at", "updated_at"]
    resolved_serializer = serializer or serializer_for(model)

    class AutoViewSet(TenantViewSet):
        queryset = model.objects.all()
        serializer_class = resolved_serializer
        search_fields = resolved_search_fields
        ordering_fields = resolved_ordering_fields

    AutoViewSet.__name__ = f"{model.__name__}ViewSet"
    return AutoViewSet
