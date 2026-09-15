from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import OrganizationRegisterSerializer, ProfileSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = OrganizationRegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    def get_object(self):
        return self.request.user


class LogoutView(generics.GenericAPIView):
    def post(self, request):
        return Response({"success": True})


login_view = TokenObtainPairView.as_view()
refresh_view = TokenRefreshView.as_view()
