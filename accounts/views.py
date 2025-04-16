from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from django.contrib.auth import login

class SignupAPIView(APIView):
    def post (self, request):
        serializer = SignupSerializer (data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response ({"message":'Usuário criado com sucesso.'}, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Create your views here.
