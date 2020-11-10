from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()

class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model=User
         fields=('email','password') 
class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model=User
        fields=('email','first_name','last_name','password','password2')
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        user=User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'passwords not match'})
        user.set_password(password)
        user.save()
        return user