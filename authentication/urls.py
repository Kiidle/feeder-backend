from django.urls import path

from . import views
from .views import assignmod
from .views import SignUpView
from .views import UserCommentariesView
from .views import UsersView
from .views import UserUpdateGroupDetail
from .views import UserUpdateView
from .views import UserView
from .views import UserWarnsView
from .views import verify_user
from .views import WarnCreateView
from .views import UsersAPIView
from .views import UserAPIView
from .views import UserAPICreateView
from .views import UserAPIUpdateView
from .views import UserAPIDeleteView


urlpatterns = [
    path("api/users", UsersAPIView.as_view(), name="users_api"),
    path("api/users/<int:pk>", UserAPIView.as_view(), name="user_api"),
    path("api/users/create", UserAPICreateView.as_view(), name="user_api_create"),
    path("api/users/<int:pk>/update", UserAPIUpdateView.as_view(), name="user_api_update"),
    path("api/users/<int:pk>/delete", UserAPIDeleteView.as_view(), name="user_api_delete"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", views.custom_logout, name="logout"),
    path("login/", views.sign_in, name="login"),
    path("users/", UsersView.as_view(), name="users"),
    path("users/<int:pk>", UserView.as_view(), name="user"),
    path(
        "users/<int:pk>/commentaries",
        UserCommentariesView.as_view(),
        name="user_commentaries",
    ),
    path("users/<int:pk>/warns", UserWarnsView.as_view(), name="user_warns"),
    path("users/<int:pk>/update", UserUpdateView.as_view(), name="user_update"),
    path(
        "users/<int:pk>/update/groups",
        UserUpdateGroupDetail.as_view(),
        name="user_group",
    ),
    path("users/<int:user_id>/update/groups/verify", verify_user, name="verify_user"),
    path("users/<int:user_id>/update/groups/moderator", assignmod, name="assignmod"),
    path("users/<int:pk>/delete", views.user_delete, name="user_delete"),
    path("users/<int:user_id>/warns/create", WarnCreateView.as_view(), name="warn_create"),
    path("warns/<int:pk>/delete", views.warn_delete, name="warn_delete"),
    path("feeds/", views.redirectURL, name="redirect_feeds"),
]
