from django.urls import path

from . import views

from .views import SignUpView, UsersView, UserView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", views.custom_logout, name="logout"),
    path("login/", views.sign_in, name="login"),
    path("users/", UsersView.as_view(), name="users"),
    path("users/<slug:pk>", UserView.as_view(), name="user")
]