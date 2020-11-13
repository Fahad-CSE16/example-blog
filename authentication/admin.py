from django.contrib import admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
User=get_user_model()
from .forms import UserChangeForm
class UserAdmin(BaseUserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    list_display=('email','first_name','last_name','is_active','is_staff','is_admin')
    fieldsets = (
        (None, {
            "fields": (
                'email','first_name','last_name','password','is_active'
            ),
        }),
        (
            "permissions",{'fields': ('is_admin','is_staff')}
        )

    )
    add_fieldsets=(
        (None, {
            "fields": (
                'email','first_name','last_name','password1','password2','is_active'
            ),
        }),
        (
            "permissions",{'fields': ('is_admin','is_staff')}
        )
    )
    ordering=('email',)
    search_fields=('email',)
    filter_horizontal=()
    list_filter=('is_admin',)

    


admin.site.register(User,UserAdmin)