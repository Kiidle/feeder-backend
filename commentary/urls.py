from django.urls import path

from . import views
from .views import CommentaryCreateView
from .views import CommentaryUpdateView
from .views import CommentaryView
from .views import CommentaryAPIView

urlpatterns = [
    path("api/commentaries/<int:pk>", CommentaryAPIView.as_view(), name="commentary_api"),
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
