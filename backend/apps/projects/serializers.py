from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    progress = serializers.IntegerField(read_only=True)
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ("organization", "created_at", "updated_at")
