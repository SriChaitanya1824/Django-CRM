from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services import export_contacts, import_contacts


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def contacts_import(request):
    org = request.user.memberships.filter(status="active").first().organization
    upload = request.FILES["file"]
    return Response(import_contacts(organization=org, csv_text=upload.read().decode("utf-8"), owner=request.user))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def contacts_export(request):
    org = request.user.memberships.filter(status="active").first().organization
    return Response({"csv": export_contacts(organization=org)})
