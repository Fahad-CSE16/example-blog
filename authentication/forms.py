from django.contrib.auth.forms import UserCreationForm, UserChangeForm as BaseUserChangeForm
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields= ('first_name','last_name','email')
class UserChangeForm(BaseUserChangeForm):
    password= forms.ReadOnlyPasswordHashField()
    class Meta:
        model=User
        fields='__all__'
