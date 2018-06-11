from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from calc_app.models import User, Operation

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Operation)
