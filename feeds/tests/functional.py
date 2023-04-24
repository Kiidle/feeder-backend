from unittest import TestCase

from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client

from feeds.models import Feed


User = get_user_model()


class FeedTestCase(TestCase):
    def test_view_feeds(self):
        clio = Client()

        user = User.objects.create(username="view.feeds", email="view.feeds@test.test", password="viewfeeds")
        user.user_permissions.add(Permission.objects.get(codename="view_feed"))
        clio.force_login(user)

        Feed.objects.create(text="Test Feed", author=user)

        response = clio.get("/", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text="Test Feed"), "Test Feed")

    def test_view_feed(self):
        clio = Client()

        user = User.objects.create(username="view.feed", email="view.feed@test.test", password="viewfeed")
        user.user_permissions.add(Permission.objects.get(codename="view_feed"))
        clio.force_login(user)

        feed = Feed.objects.create(text="Test Feed", author=user)
        response = clio.get(f"/feeds/{feed.id}", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text="Test Feed"), "Test Feed")
