from django.urls import path

from .views import CommentaryView, CommentaryCreateView
from . import views

urlpatterns = [
    path("feeds/<int:feed_id>/commentaries/create.html", CommentaryCreateView.as_view(), name="commentary_create"),
    path("commentaries/<slug:pk>", CommentaryView.as_view(), name="commentary"),
    path("commentaries/<slug:pk>/delete", views.commentary_delete, name="commentary_delete")
]