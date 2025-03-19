from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Inscription
from .serializers import InscriptionSerializer

class InscriptionViewSet (ModelViewSet):
    queryset = Inscription.objects.all ()
    serializer_class = InscriptionSerializer

# Create your views here.
