from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import StudentSerializer, GuardianSerializer
from .models import Student, Guardian


class ApiRootView(generics.ListAPIView):
    def get(self, request):
        return Response({
            "message": "Welcome to the Campus_7's API!",
            "available_endpoints": {
                "school": "/api/v1/all/",
                "admin": "http://localhost:8000/admin/",
                "auth": "http://localhost:8000/auth/",
                "student": "http://localhost:8000/api/v1/students/",
                "guardian": "http://8000/api/v1/guardians",
            }
        })
    
class StudentsAPIView (generics.ListCreateAPIView):
    queryset = Student.objects.all ()
    serializer_class = StudentSerializer

class StudentAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all ()
    serializer_class = StudentSerializer
    

class GuardiansAPIView (generics.ListCreateAPIView):
    queryset = Student.objects.all ()
    serializer_class = GuardianSerializer
    
class GuardianAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all ()
    serializer_class = GuardianSerializer

    
     



# Create your views here.
