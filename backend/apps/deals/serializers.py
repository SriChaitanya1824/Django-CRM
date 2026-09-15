from rest_framework import serializers

from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    weighted_pipeline_value = serializers.DecimalField(max_digits=14, decimal_places=2, read_only=True)
    class Meta:
        model = Deal
        fields = "__all__"
        read_only_fields = ("organization", "created_at", "updated_at")
