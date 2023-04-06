from django.db import models

from authentication.blacklist import is_blacklisted, censorer
from authentication.models import User, Warn
from feeds.models import Feed


class Commentary(models.Model):
    text = models.TextField(max_length=200)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="commentaries")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentaries")

    def save(self, *args, **kwargs):
        if is_blacklisted(self.text):
            self.text = censorer(self.text)
            Warn.objects.create(user=self.author, reason="Wortwahl")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
