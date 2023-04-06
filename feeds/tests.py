from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Feed

User = get_user_model()


class FeedTestCase(TestCase):
    def setUp(self):
        feedAuthor = User.objects.create(username="feed.author", email="feed.author@test.test")
        self.feed = Feed.objects.create(text="Test feed", author=feedAuthor)

    def test_feed_text(self):
        self.assertEqual(self.feed.text, "Test feed", "Feed Text not Equal")

    def test_feed_create(self):
        initial_count = Feed.objects.count()
        self.assertEqual(Feed.objects.count(), initial_count)

        feedAuthor = User.objects.create(username="feed.creator", email="feed.creator@test.test")
        Feed.objects.create(text="Test feed", author=feedAuthor)

        self.assertEqual(Feed.objects.count(), initial_count + 1)

    def test_feed_update(self):
        self.feed.text = "Updated test feed"
        self.feed.save()

        self.assertEqual(self.feed.text, "Updated test feed", "Feed Text not updated")

    def test_feed_delete(self):
        feed = Feed.objects.get(text="Test feed")
        feed.delete()
        with self.assertRaises(Feed.DoesNotExist):
            Feed.objects.get(text="Test feed")
