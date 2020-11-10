from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.reverse import reverse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework import permissions, viewsets
from rest_framework import generics,status
from .seriaizers import LoginSerializer,RegisterSerializer
from django.contrib.auth import get_user_model,login,authenticate
User=get_user_model()


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'logins': reverse('logins', request=request, format=format),
           
        })
# Create your views here.
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class LoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        if email and password:
            user_obj = User.objects.filter(email__iexact=email)
            if user_obj.exists() and user_obj.first().check_password(password):
                user = LoginSerializer(user_obj)
                data_list = {}
                data_list.update(user.data)
                return Response({"message": "Login Successfully", "data":data_list, "code": 200})
            else:
                message = "Unable to login with given credentials"
                return Response({"message": message , "code": 500, 'data': {}} )
        else:
            
            message = "Invalid login details."
        return Response({"message": message , "code": 500, 'data': {}})
@api_view(['POST',])
def registration_view(request):
    if request.method== 'POST':
        serializer=RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user=serializer.save()
            data['response'] ="Successfully registered a new user"
            data['email']=user.email
            data['first_name']=user.first_name
            data['last_name']=user.last_name
        else:
            data=serializer.errors
        return Response(data)