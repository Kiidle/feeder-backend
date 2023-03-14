from django.db import models

from authentication.models import User
from feeds.models import Feed


class Commentary(models.Model):
    text = models.TextField(max_length=200)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="commentaries")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentaries")

    class Meta:
        ordering = ['-id']