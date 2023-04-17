from django.contrib.auth import get_user_model
from django.db import models

from authentication.blacklist import censorer, is_blacklisted
from authentication.models import Warn

User = get_user_model()


class Feed(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="feeds",
    )

    def save(self, *args, **kwargs):
        if is_blacklisted(self.text):
            self.text = censorer(self.text)
            Warn.objects.create(user=self.author, reason="Wortwahl")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]
