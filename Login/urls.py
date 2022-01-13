from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path("Login",LoginView.as_view(),name="login"),
    path("Logout",LogoutView.as_view(next_page="home"),name="logout")
]