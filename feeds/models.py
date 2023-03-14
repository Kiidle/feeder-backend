from django.db import models

from authentication.models import User


# Create your models here.

class Feed(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="feeds",
    )
    class Meta:
        ordering = ['-id']