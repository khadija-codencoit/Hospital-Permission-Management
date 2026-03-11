from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *

# Create your views here.

class AuthViewSet(viewsets.ViewSet):

    def register(self,request):
        serializers = RegistrationSerializer(data = request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response(UserSerializer(user).data)



