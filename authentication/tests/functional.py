from unittest import TestCase

from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client

from authentication.models import Warn
from commentary.models import Commentary
from feeds.models import Feed

User = get_user_model()


class UserTestCase(TestCase):
    def test_view_user(self):
        clio = Client()

        user = User.objects.create(username='view.user', email='view.user@test.test', password='viewuser')
        user.user_permissions.add(Permission.objects.get(codename='view_user'))
        user.user_permissions.add(Permission.objects.get(codename='view_feed'))
        clio.force_login(user)

        Feed.objects.create(text='Test Feed', author=user)

        response = clio.get(f"/users/{user.id}", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text='view.user@test.test'), 'view.user@test.test')
        self.assertEqual(soup.find(text='Test Feed'), 'Test Feed')

    def test_view_user_commentaries(self):
        clio = Client()

        user = User.objects.create(username='view.user.commentaries', email='view.user.commentaries@test.test',
                                   password='viewusercommentaries')
        user.user_permissions.add(Permission.objects.get(codename='view_user'))
        user.user_permissions.add(Permission.objects.get(codename='view_feed'))
        user.user_permissions.add(Permission.objects.get(codename='view_commentary'))
        clio.force_login(user)

        feed = Feed.objects.create(text='Test Feed', author=user)
        Commentary.objects.create(text='Test Commentary', feed=feed, author=user)

        response = clio.get(f"/users/{user.id}/commentaries", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text='view.user.commentaries@test.test'), 'view.user.commentaries@test.test')
        self.assertEqual(soup.find(text='Test Feed'), 'Test Feed')
        self.assertEqual(soup.find(text='Test Commentary'), 'Test Commentary')

    def test_view_user_warns(self):
        clio = Client()

        user = User.objects.create(username='view.user.warns', email='view.user.warns@test.test',
                                   password='viewuserwarns')
        user.user_permissions.add(Permission.objects.get(codename='view_user'))
        user.user_permissions.add(Permission.objects.get(codename='view_warn'))
        clio.force_login(user)

        Warn.objects.create(reason='Fake news', user=user)

        response = clio.get(f"/users/{user.id}/warns", follow=True)
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)

        self.assertEqual(soup.find(text='view.user.warns@test.test'), 'view.user.warns@test.test')
        self.assertEqual(soup.find(text='Fake news'), 'Fake news')
