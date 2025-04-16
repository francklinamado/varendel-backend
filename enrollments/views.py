from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentsViewSet (ModelViewSet):
    queryset =  Enrollment.objects.all ()
    serializer_class = EnrollmentSerializer
