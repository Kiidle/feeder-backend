from django.contrib import admin

from authentication.models import Role
# Register your models here.
from authentication.models import User
from authentication.models import Warn

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Warn)
