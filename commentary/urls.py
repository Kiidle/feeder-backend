from django.urls import path

from .views import CommentaryView
from . import views

urlpatterns = [
<<<<<<< Updated upstream
=======
    path("feeds/<int:feed_id>/commentaries/create", CommentaryCreateView.as_view(), name="commentary_create"),
>>>>>>> Stashed changes
    path("commentaries/<slug:pk>", CommentaryView.as_view(), name="commentary"),
    path("commentaries/<slug:pk>/delete", views.commentary_delete, name="commentary_delete")
]