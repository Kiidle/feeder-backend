from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name=_("Vorname"))
    last_name = models.CharField(max_length=100, verbose_name=_("Nachname"))
    username = models.EmailField(unique=True, verbose_name="Benutzername")
    email = models.EmailField(unique=True, verbose_name="E-Mail Adresse")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    birthdate = models.DateField(null=True, verbose_name=_("Geburtsdatum"))
    verified = models.BooleanField(null=True)

class Warn(models.Model):
    class Reasons(models.TextChoices):
        MISINFORMATION = _("Falschinformationen"), _("Falschinformationen")
        ABUSE = _("Missbrauch von Privilegien"), _("Missbrauch von Privilegien")
        HARASSMENT = _("Belästigung"), _("Belästigung")
        BULLYING = _("Cybermobing"), _("Cybermobbing")
        GROOMING = _("Cybergrooming"), _("Cybergrooming")
        WHATABOUTISM = _("Whataboutismus"), _("Whataboutismus")
        RELATIVISATION = _("Relativierung"), _("Relativierung")
        BLACKMAILING = _("Erpressung"), _("Erpressung")
        THREAT = _("Drohung"), _("Drohung")
        COW = _("Wortwahl"), _("Wortwahl")
        HATESPEECH = _("Hassrede"), _("Hassrede")
        SWEARWORD = _("Beleidigung"), _("Beleidigung")
        DISCRIMINATION = _("Diskriminierung"), _("Diskriminierung")
        SEXISM = _("Sexismus"), _("Sexismus")
        RACISM = _("Rassismus"), _("Rassismus")
        FACISM = _("Faschismus"), _("Faschismus")
        ANTISEMITISM = _("Antisemitismus"), _("Antisemitismus")
        SCAM = _("Betrug"), _("Betrug")
        SPAM = _("Spam"), _("Spam")

    reason = models.CharField(max_length=30, choices=Reasons.choices, default=Reasons.HATESPEECH, verbose_name=_("Grund"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")
