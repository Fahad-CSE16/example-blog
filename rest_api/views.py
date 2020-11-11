from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriaizers import RegisterSerializer
from django.contrib.auth import get_user_model
User=get_user_model()
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
