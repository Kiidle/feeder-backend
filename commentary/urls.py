from django.urls import path

from . import views
from .views import CommentaryCreateView
from .views import CommentaryUpdateView
from .views import CommentaryView
from .views import CommentariesAPIView
from .views import CommentaryAPIView
from .views import CommentaryCreateAPIView
from .views import CommentaryUpdateAPIView
from .views import CommentaryDeleteAPIView

urlpatterns = [
    path("api/commentaries", CommentariesAPIView.as_view(), name="commentaries_api"),
    path("api/commentaries/<int:pk>", CommentaryAPIView.as_view(), name="commentary_api"),
    path("api/feeds/<int:feed_id>/commentaries/create", CommentaryCreateAPIView.as_view(), name="commentary_api_create"),
    path("api/commentaries/<int:pk>/update", CommentaryUpdateAPIView.as_view(), name="commentary_api_update"),
    path("api/commentaries/<int:pk>/delete", CommentaryDeleteAPIView.as_view(), name="commentary_api_delete"),
    path(
        "feeds/<int:feed_id>/commentaries/create",
        CommentaryCreateView.as_view(),
        name="commentary_create",
    ),
    path("commentaries/<int:pk>", CommentaryView.as_view(), name="commentary"),
    path(
        "commentaries/<int:pk>/update",
        CommentaryUpdateView.as_view(),
        name="commentary_update",
    ),
    path(
        "commentaries/<int:pk>/delete",
        views.commentary_delete,
        name="commentary_delete",
    ),
]
