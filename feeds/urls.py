from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import FeedsView, FeedView

urlpatterns = [
    path("", login_required(FeedsView.as_view()), name="feeds"),
    path("feeds/<slug:pk>", FeedView.as_view(), name="feed")
]