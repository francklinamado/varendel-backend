from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer, GuardianSerializer
from .models import Student, Guardian


class ApiRootView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the API!",
            "available_endpoints": {
                "school": "/api/v1/all/",
                "admin": "http://localhost:8000/admin/",
                "auth": "http://localhost:8000/auth/",
                "student": "http://localhost:8000/api/v1/student/",
                "guardian": "http://8000/api/v1/guardian",
            }
        }, status=status.HTTP_200_OK)
class StudentAPIView (APIView):
    def get (self, request):
        students = Student.objects.all ()
        serializer = StudentSerializer (students, many = True)
        return Response (serializer.data)
    def post (self, request):
        serializer = StudentSerializer (data= request.data)
        if serializer.is_valid ():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuardianAPIView (APIView):

    def get (self, request):
        guardians = Guardian.objects.all ()
        serializer = GuardianSerializer (guardians, many= True)
        return Response (serializer.data)
     



# Create your views here.
