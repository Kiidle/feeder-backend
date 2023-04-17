from unittest import TestCase

from django.contrib.auth import get_user_model

from feeds.models import Feed

User = get_user_model()


class FeedTestCase(TestCase):
    def setUp(self):
        self.feedAuthor = User.objects.create(username="feed.author", email="feed.author@test.test")

    def test_censores_text_on_feed(self):
        self.assertEqual(self.feedAuthor.warns.count(), 0)
        feed = Feed.objects.create(text="Arsch du Hure", author=self.feedAuthor)
        self.assertEqual(feed.text, "***** du ****")
        self.assertEqual(self.feedAuthor.warns.count(), 1)
