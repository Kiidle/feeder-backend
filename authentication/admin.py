from django.contrib import admin

# Register your models here.
from authentication.models import User
from authentication.models import Warn

admin.site.register(User)
admin.site.register(Warn)