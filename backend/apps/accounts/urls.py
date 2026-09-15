from django.urls import path

from .views import LogoutView, ProfileView, RegisterView, login_view, refresh_view

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", login_view),
    path("token/refresh/", refresh_view),
    path("logout/", LogoutView.as_view()),
    path("profile/", ProfileView.as_view()),
]
