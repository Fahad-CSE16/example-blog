from django.contrib import admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)

# Register your models here.
from django.contrib.auth import get_user_model
User=get_user_model()
admin.site.register(User)