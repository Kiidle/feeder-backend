from django.test import TestCase
from .models import User, Role, Warn

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email = "test@test.test",
            username = "testuser",
            password = "testpassword",
            birthdate = "2000-01-01",
            verified = True
        )

    def test_user_create(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(str(self.user), self.user.email)

    def test_user_roles(self):
        role = Role.objects.create(prefix="admin")
        self.user.roles.add(role)
        self.assertTrue(role in self.user.roles.all())

    def test_user_read_warns(self):
        warn = Warn.objects.create(reason="Bad behavior", user=self.user)
        self.assertTrue(warn in self.user.warns.all())