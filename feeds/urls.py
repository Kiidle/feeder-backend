from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import FeedsView, FeedView, FeedCreateView, FeedUpdateView
from . import views

urlpatterns = [
    path("", login_required(FeedsView.as_view()), name="feeds"),
    path("feeds/create", FeedCreateView.as_view(), name="feed_create"),
    path("feeds/<slug:pk>", FeedView.as_view(), name="feed"),
    path("feeds/<slug:pk>/update", FeedUpdateView.as_view(), name='feed_update'),
    path("feeds/<slug:pk>/delete", views.feed_delete, name="feed_delete")
]