# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import serializers,status
from rest_framework.response import Response

from .serializers import UserSerializer,ProfileSerializer,RegistrationSerializer
from . models import Profile
from django.contrib.auth.models import User

# Create your views here.

class RegistrationView(APIView):
    def post(self,request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


