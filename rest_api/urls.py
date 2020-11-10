from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register(r'login/', LoginView)


urlpatterns = [
    path('login/',LoginView.as_view(), name='logins'),
    path('register/',registration_view, name='register'),
    path('', include(router.urls)),
]