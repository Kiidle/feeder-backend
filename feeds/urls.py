from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import FeedCreateView
from .views import FeedsView
from .views import FeedUpdateView
from .views import FeedView


urlpatterns = [
    path("", login_required(FeedsView.as_view()), name="feeds"),
    path("feeds/create", FeedCreateView.as_view(), name="feed_create"),
    path("feeds/<int:pk>", FeedView.as_view(), name="feed"),
    path("feeds/<int:pk>/update", FeedUpdateView.as_view(), name="feed_update"),
    path("feeds/<int:pk>/delete", views.feed_delete, name="feed_delete"),
]
