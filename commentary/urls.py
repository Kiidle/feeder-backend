from django.urls import path

from .views import CommentaryView

urlpatterns = [
    path("commentaries/<slug:pk>", CommentaryView.as_view(), name="commentary")
]