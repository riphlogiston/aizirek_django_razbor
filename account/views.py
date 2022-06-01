from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegistrationSerializer

class RegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message='''
            You're done!
            '''
        return Response(message)
