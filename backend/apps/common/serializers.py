from rest_framework import serializers

from .models import Activity, Tag


class TenantSerializerMixin:
    def validate(self, attrs):
        request = self.context.get("request")
        org = self.context.get("organization")
        if request and org and not request.user.memberships.filter(organization=org, status="active").exists():
            raise serializers.ValidationError("Invalid organization context.")
        return super().validate(attrs)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ("organization",)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
        read_only_fields = ("organization", "actor")
