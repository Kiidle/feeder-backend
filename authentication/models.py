from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    prefix = models.CharField(max_length=15)

    def __str__(self):
        return self.prefix

class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    birthdate = models.DateField(null = True)
    verified = models.BooleanField(null = True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name="roles", null=True, blank=True)

class Warn(models.Model):
    reason = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")