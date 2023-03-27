from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Feed, Commentary

User = get_user_model()
class CommentaryTestCase(TestCase):
    def setUp(self):
        feedAuthor = User.objects.create(username="feed.author", email="feed.author@test.test")
        commentaryAuthor = User.objects.create(username="commentary.author@test.test")
        feed = Feed.objects.create(text="Test feed", author=feedAuthor)
        Commentary.objects.create(text="Test commentary", feed=feed, author=commentaryAuthor)

    def test_commentary_text(self):
        commentary = Commentary.objects.get(text="Test commentary")
        self.assertEqual(commentary.text, "Test commentary", "Commentary Text not Equal")

    def test_commentary_create(self):
        initial_count = Commentary.objects.count()

        self.assertEqual(Feed.objects.count(), initial_count)

        feedAuthor = User.objects.create(username="feed.creator", email="feed.creator@test.test")
        feed = Feed.objects.create(text="Test feed", author=feedAuthor)
        commentaryAuthor = User.objects.create(username="commentary.creator", email="commentary.creator@test.test")
        Commentary.objects.create(text="Test commentary", feed=feed, author=commentaryAuthor)

        self.assertEqual(Commentary.objects.count(), initial_count + 1)

    def test_commentary_update(self):
        commentary = Commentary.objects.get(text="Test commentary")
        commentary.text = "Updated test commentary"
        commentary.save()

        updated_commentary = Commentary.objects.get(pk=commentary.pk)
        self.assertEqual(updated_commentary.text, "Updated test commentary", "Commentary Text not updated")

    def test_commentary_delete(self):
        commentary = Commentary.objects.get(text="Test commentary")
        commentary.delete()
        with self.assertRaises(Commentary.DoesNotExist):
            Commentary.objects.get(text="Test commentary")