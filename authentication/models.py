from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birthdate = models.DateField(null = True)
    verified = models.BooleanField(null = True)

class Warn(models.Model):
    reason = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")