from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import FeedCreateView
from .views import FeedsView
from .views import FeedUpdateView
from .views import FeedView
from .views import FeedsViewSet
from .views import FeedViewSet
from .views import FeedCreateAPIView


urlpatterns = [
    path("", login_required(FeedsView.as_view()), name="feeds"),
    path("api/feeds", FeedsViewSet.as_view({'get': 'list', 'post': 'create'}), name="feeds_api"),
    path("api/feeds/<int:pk>", FeedViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="feeds_api_detail"),
    path("feeds/create", FeedCreateView.as_view(), name="feed_create"),
    path("feeds/<int:pk>", FeedView.as_view(), name="feed"),
    path("feeds/<int:pk>/update", FeedUpdateView.as_view(), name="feed_update"),
    path("feeds/<int:pk>/delete", views.feed_delete, name="feed_delete"),
]