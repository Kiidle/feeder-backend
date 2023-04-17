from django.contrib.auth import get_user_model
from django.test import TestCase

from authentication.blacklist import is_blacklisted, censorer
from feeds.models import Feed

User = get_user_model()


class FeedTestCase(TestCase):
    def setUp(self):
        self.feedAuthor = User.objects.create(username="feed.author", email="feed.author@test.test")
        self.feed = Feed.objects.create(text="Test feed", author=self.feedAuthor)

    def test_feed_text(self):
        self.assertEqual(self.feed.text, "Test feed", "Feed Text not Equal")

    def test_feed_create(self):
        initial_count = Feed.objects.count()
        self.assertEqual(Feed.objects.count(), initial_count)

        Feed.objects.create(text="Test feed", author=self.feedAuthor)

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

    def test_censored(self):
        self.assertTrue(is_blacklisted("Arsch du Hure"))
        self.assertFalse(is_blacklisted("Hallo"))

        self.assertEqual(censorer("Arsch du Hure"), "***** du ****")
        self.assertEqual(censorer("Hallo"), "Hallo")
