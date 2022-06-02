from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView



from .serializers import *

User=get_user_model()

class RegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message='''
            You're done!
            '''
        return Response(message)


class ActivationView(APIView):
    def get(self, request, activation_code):
        user=get_object_or_404(User,activation_code=activation_code)
        user.is_active=True
        user.activation_code=''
        user.save()
        return Response('Your account is successfully activated', status=status.HTTP_200_OK)


        # get_object_or_404 - посмотреть, как работает
        #log out в jwt не используют, токен удаляется фронтом из localstorage при выходе с аккаунта

class LoginView (TokenObtainPairView):
    serializer_class=LoginSerializer

