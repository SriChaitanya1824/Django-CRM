from apps.common.crud import viewset_for

from .models import Project
from .serializers import ProjectSerializer

ProjectViewSet = viewset_for(Project, ProjectSerializer, ["name", "description"])
