from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import FeedCreateView
from .views import FeedsView
from .views import FeedUpdateView
from .views import FeedView
from .views import FeedsAPIView
from .views import FeedAPIView
from .views import FeedCreateAPIView
from .views import FeedUpdateAPIView
from .views import FeedDeleteAPIView


urlpatterns = [
    path("", login_required(FeedsView.as_view()), name="feeds"),
    path("api/feeds", FeedsAPIView.as_view(), name="feeds_api"),
    path("api/feeds/<int:pk>", FeedAPIView.as_view(), name="feeds_api_detail"),
    path("api/feeds/create", FeedCreateAPIView.as_view(), name="feed_api_create"),
    path("api/feeds/<int:pk>/update", FeedUpdateAPIView.as_view(), name="feed_api_update"),
    path("api/feeds/<int:pk>/delete", FeedDeleteAPIView.as_view(), name="feed_api_delete"),
    path("feeds/create", FeedCreateView.as_view(), name="feed_create"),
    path("feeds/<int:pk>", FeedView.as_view(), name="feed"),
    path("feeds/<int:pk>/update", FeedUpdateView.as_view(), name="feed_update"),
    path("feeds/<int:pk>/delete", views.feed_delete, name="feed_delete"),
]