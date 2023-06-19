import random
import string
import uuid
from unittest import TestCase

from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from authentication.models import Warn
from django.contrib.contenttypes.models import ContentType
from authentication.serializers import UserSerializer
from commentary.models import Commentary
from feeds.models import Feed

User = get_user_model()


class UserTestCase(TestCase):
    def test_view_user(self):
        clio = Client()

        user = User.objects.create(username="view.user", email="view.user@test.test", password="viewuser")
        user.user_permissions.add(Permission.objects.get(codename="view_user"))
        user.user_permissions.add(Permission.objects.get(codename="view_feed"))
        clio.force_login(user)

        Feed.objects.create(text="Test Feed", author=user)

        response = clio.get(f"/users/{user.id}", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text="view.user@test.test"), "view.user@test.test")
        self.assertEqual(soup.find(text="Test Feed"), "Test Feed")

    def test_view_user_commentaries(self):
        clio = Client()

        user = User.objects.create(
            username="view.user.commentaries",
            email="view.user.commentaries@test.test",
            password="viewusercommentaries",
        )
        user.user_permissions.add(Permission.objects.get(codename="view_user"))
        user.user_permissions.add(Permission.objects.get(codename="view_feed"))
        user.user_permissions.add(Permission.objects.get(codename="view_commentary"))
        clio.force_login(user)

        feed = Feed.objects.create(text="Test Feed", author=user)
        Commentary.objects.create(text="Test Commentary", feed=feed, author=user)

        response = clio.get(f"/users/{user.id}/commentaries", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(
            soup.find(text="view.user.commentaries@test.test"),
            "view.user.commentaries@test.test",
        )
        self.assertEqual(soup.find(text="Test Feed"), "Test Feed")
        self.assertEqual(soup.find(text="Test Commentary"), "Test Commentary")

    def test_view_user_warns(self):
        clio = Client()

        user = User.objects.create(
            username="view.user.warns",
            email="view.user.warns@test.test",
            password="viewuserwarns",
        )
        user.user_permissions.add(Permission.objects.get(codename="view_user"))
        user.user_permissions.add(Permission.objects.get(codename="view_warn"))
        clio.force_login(user)

        Warn.objects.create(reason="Fake news", user=user)

        response = clio.get(f"/users/{user.id}/warns", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text="view.user.warns@test.test"), "view.user.warns@test.test")
        self.assertEqual(soup.find(text="Fake news"), "Fake news")


class UsersViewSetTest(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuserapi@django.com',
            email='testuserapi@django.com',
            password='testpassword'
        )

        # Grant required permissions to the user
        content_type = ContentType.objects.get_for_model(User)
        view_permission = Permission.objects.get(content_type=content_type, codename='view_user')
        add_permission = Permission.objects.get(content_type=content_type, codename='add_user')
        change_permission = Permission.objects.get(content_type=content_type, codename='change_user')
        delete_permission = Permission.objects.get(content_type=content_type, codename='delete_user')
        self.user.user_permissions.add(view_permission, add_permission, change_permission, delete_permission)

    def test_list_users(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('users_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('users_api')
        data = {
            'username': 'newuser@example.com',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'first_name': 'New',
            'last_name': 'User',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['username'], 'newuser@example.com')
        self.assertEqual(response.data['email'], 'newuser@example.com')
        self.assertEqual(response.data['first_name'], 'New')
        self.assertEqual(response.data['last_name'], 'User')

class UserViewSetTest(APITestCase):
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

    def test_retrieve_user(self):
        self.client.force_authenticate(user=self.user)

        user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        url = reverse('user_api', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser@example.com')
        self.assertEqual(response.data['email'], 'testuser@example.com')
        self.assertEqual(response.data['first_name'], 'Test')
        self.assertEqual(response.data['last_name'], 'User')

    def test_update_user(self):
        self.client.force_authenticate(user=self.user)

        user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        url = reverse('user_api', kwargs={'pk': user.pk})
        data = {
            'username': 'updateduser@example.com',
            'email': 'updateduser@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'updateduser@example.com')
        self.assertEqual(response.data['email'], 'updateduser@example.com')
        self.assertEqual(response.data['first_name'], 'Updated')
        self.assertEqual(response.data['last_name'], 'User')

    def test_delete_user(self):
        self.client.force_authenticate(user=self.user)

        user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )
        url = reverse('user_api', kwargs={'pk': user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=user.pk).exists())