from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
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
                "guardian": "http://localhost:8000/api/v1/guardians",
            }
        })
    
#===================== API V1 ============================

    
class StudentsAPIView (generics.ListCreateAPIView):
    queryset = Student.objects.all ()
    serializer_class = StudentSerializer

    def get_queryset(self):
        guardian_pk = self.kwargs.get ('pk')
        return Student.objects.filter (guardian_id=guardian_pk)

class StudentAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all ()
    serializer_class = StudentSerializer
    

class GuardiansAPIView (generics.ListCreateAPIView):
    queryset = Guardian.objects.all ()
    serializer_class = GuardianSerializer

    
    
class GuardianAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Guardian.objects.all ()
    serializer_class = GuardianSerializer


#===================== API V2 ============================

class StudentViewSet (ModelViewSet):
    queryset = Student.objects.all ()
    serializer_class = StudentSerializer
    @action (detail = True, methods = ['get'])
    def guardians (self,request, pk = None):
                student = self.get_object()
                guardians = [student.guardian]
                serializer = GuardianSerializer (guardians, many = True)
                return Response (serializer.data)




class GuardianViewSet(ModelViewSet):    
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

    @action(detail=True, methods=['get'])
    def students (self, request, pk = None):
        guardian = self.get_object()
        students = guardian.students.all () 
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)  




# Create your views here.
