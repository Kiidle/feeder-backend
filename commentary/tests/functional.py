from unittest import TestCase

from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client

from commentary.models import Commentary
from feeds.models import Feed

User = get_user_model()


class CommentaryTestCase(TestCase):
    def test_view_commentaries(self):
        clio = Client()

        user = User.objects.create(
            username="view.commentaries",
            email="view.commentaries@test.test",
            password="viewcommentaries",
        )
        user.user_permissions.add(Permission.objects.get(codename="view_feed"))
        user.user_permissions.add(Permission.objects.get(codename="view_commentary"))
        clio.force_login(user)

        feed = Feed.objects.create(text="Test Feed", author=user)
        Commentary.objects.create(text="Test Commentary One", feed=feed, author=user)
        Commentary.objects.create(text="Test Commentary Two", feed=feed, author=user)

        response = clio.get(f"/feeds/{feed.id}", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text="Test Commentary One"), "Test Commentary One")
        self.assertEqual(soup.find(text="Test Commentary Two"), "Test Commentary Two")

    def test_view_commentary(self):
        clio = Client()

        user = User.objects.create(
            username="view.commentary",
            email="view.commentary@test.test",
            password="viewcommentary",
        )
        user.user_permissions.add(Permission.objects.get(codename="view_feed"))
        user.user_permissions.add(Permission.objects.get(codename="view_commentary"))
        clio.force_login(user)

        feed = Feed.objects.create(text="Test Feed", author=user)
        commentary = Commentary.objects.create(
            text="Test Commentary", feed=feed, author=user
        )

        response = clio.get(f"/commentaries/{commentary.id}", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text="Test Commentary"), "Test Commentary")
