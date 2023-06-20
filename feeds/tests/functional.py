from unittest import TestCase

from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status

from feeds.models import Feed

User = get_user_model()


class FeedTestCase(TestCase):
    User.objects.all().delete()

    def test_view_feeds(self):
        clio = Client()

        user = User.objects.create(username="view.feeds@test.test", email="view.feeds@test.test", password="viewfeeds")
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


class APIClient:
    pass


class APITestCase:
    pass


class FeedsViewSetTest(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testfeedapi@django.com',
            email='testfeedapi@django.com',
            password='testpassword'
        )

        content_type = ContentType.objects.get_for_model(User)
        view_permission = Permission.objects.get(content_type=content_type, codename='view_feed')
        add_permission = Permission.objects.get(content_type=content_type, codename='add_feed')
        change_permission = Permission.objects.get(content_type=content_type, codename='change_feed')
        delete_permission = Permission.objects.get(content_type=content_type, codename='delete_feed')
        self.user.user_permissions.add(view_permission, add_permission, change_permission, delete_permission)

    def test_list_feeds(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('feeds_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_feed(self):
        self.client.force_authenticate(user=self.user)

        url = reverse("feeds_api")
        data = {
            'text': 'content'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['text'], 'content')

class FeedViewSetTest(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuserapi2@django.com',
            email='testuserapi2@django.com',
            password='testpassword'
        )

        # Grant required permissions to the user
        content_type = ContentType.objects.get_for_model(User)
        view_permission = Permission.objects.get(content_type=content_type, codename='view_user')
        add_permission = Permission.objects.get(content_type=content_type, codename='add_user')
        change_permission = Permission.objects.get(content_type=content_type, codename='change_user')
        delete_permission = Permission.objects.get(content_type=content_type, codename='delete_user')
        self.user.user_permissions.add(view_permission, add_permission, change_permission, delete_permission)

    def test_retrieve_feed(self):
        self.client.force_authenticate(user=self.user)

        feed = Feed.objects.create_user(
            text='content',
        )
        url = reverse('feed_api', kwargs={'pk': feed.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'content')

    def test_update_feed(self):
        self.client.force_authenticate(user=self.user)

        feed = Feed.objects.create_user(
            text='content',
        )
        url = reverse('feed_api', kwargs={'pk': feed.pk})
        data = {
            'text': 'updated',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'updated')

    def test_delete_user(self):
        self.client.force_authenticate(user=self.user)

        feed = Feed.objects.create_user(
            text='content',
        )
        url = reverse('feed_api', kwargs={'pk': feed.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=feed.pk).exists())
