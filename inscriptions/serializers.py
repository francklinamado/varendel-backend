from rest_framework import serializers
from .models import Inscription

class InscriptionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = [
            'name',
            'email',
            'phone',
            'status',

        ]