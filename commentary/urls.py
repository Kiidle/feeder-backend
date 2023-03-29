from django.urls import path

from .views import CommentaryView, CommentaryCreateView, CommentaryUpdateView
from . import views

urlpatterns = [
    path("feeds/<int:feed_id>/commentaries/create", CommentaryCreateView.as_view(), name="commentary_create"),
    path("commentaries/<slug:pk>", CommentaryView.as_view(), name="commentary"),
    path("commentaries/<slug:pk>/update", CommentaryUpdateView.as_view(), name="commentary_update"),
    path("commentaries/<slug:pk>/delete", views.commentary_delete, name="commentary_delete")
]