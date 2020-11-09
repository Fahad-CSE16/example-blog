from django.urls import path
from authentication.views import loginuser, register

urlpatterns = [
    path('login/', loginuser, name='login'),
    path('register/', register, name='register'),
]
