from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from django.utils import timezone
from datetime import datetime, time
from authentication.blacklist import censorer
from authentication.blacklist import is_blacklisted
from authentication.models import Warn
from feeds.models import Feed


User = get_user_model()


class Commentary(models.Model):
    text = models.TextField(max_length=200, verbose_name=_("Inhalt"))
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="commentaries")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Veröffentlicht"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentaries")

    def time_since_published(self):
        now = timezone.now()
        diff = now - self.published_date

        if diff.days >= 365:
            count = diff.days // 365
            return _("Vor {count} Jahr{plural}").format(count=count, plural=_('e') if count > 1 else '')
        elif diff.days >= 30:
            count = diff.days // 30
            return _("Vor {count} Monat{plural}").format(count=count, plural=_('e') if count > 1 else '')
        elif diff.days > 0:
            return _("Vor {count} Tag{plural}").format(count=diff.days, plural=_('e') if diff.days > 1 else '')
        elif diff.seconds >= 3600:
            count = diff.seconds // 3600
            return _("Vor {count} Stunde{plural}").format(count=count, plural=_('n') if count > 1 else '')
        elif diff.seconds >= 60:
            count = diff.seconds // 60
            return _("Vor {count} Minute{plural}").format(count=count, plural=_('n') if count > 1 else '')
        else:
            return _("Gerade eben")

    def save(self, *args, **kwargs):
        if is_blacklisted(self.text):
            self.text = censorer(self.text)
            Warn.objects.create(user=self.author, reason="Wortwahl")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-published_date", "-id"]
