from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    prefix = models.CharField(max_length=15)

    def __str__(self):
        return self.prefix


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    birthdate = models.DateField(null=True)
    verified = models.BooleanField(null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name="roles", null=True, blank=True)


class Warn(models.Model):
    class Reasons(models.TextChoices):
        MISINFORMATION = 'Falschinformationen', _('Falschinformationen')
        ABUSE = 'Missbrauch von Privilegien', _('Missbrauch von Privilegien')
        HARASSMENT = 'Belästigung', _('Belästigung')
        BULLYING = 'Cybermobing', 'Cybermobbing'
        GROOMING = 'Cybergrooming', 'Cybergrooming'
        WHATABOUTISM = 'Whataboutismus', _('Whataboutismus')
        RELATIVISATION = 'Relativierung', _('Relativierung')
        BLACKMAILING = 'Erpressung', _('Erpressung')
        THREAT = 'Drohung', _('Drohung')
        COW = 'Wortwahl', _('Wortwahl')
        HATESPEECH = 'Hassrede', _('Hassrede')
        SWEARWORD = 'Beleidigung', _('Beleidigung')
        DISCRIMINATION = 'Diskriminierung', _('Diskriminierung')
        SEXISM = 'Sexismus', _('Sexismus')
        RACISM = 'Rassismus', _('Rassismus')
        FACISM = 'Faschismus', _('Faschismus')
        ANTISEMITISM = 'Antisemitismus', _('Antisemitismus')
        SCAM = 'Betrug', _('Betrug')
        SPAM = 'Spam', _('Spam')

    reason = models.CharField(max_length=30, choices=Reasons.choices, default=Reasons.HATESPEECH)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")
