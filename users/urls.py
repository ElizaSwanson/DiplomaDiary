from django.contrib.auth.views import LoginView
from django.urls import path

from .apps import UsersConfig
from .views import CustomLogoutView, UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(template_name="register.html"), name="register"),
]
