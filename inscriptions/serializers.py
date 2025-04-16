from rest_framework import serializers
from .models import Inscription

class InscriptionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = [
            'id',
            'full_name',
            'date_of_birth',
            'idnumber',
            'phone_number',
            'email_adress',
            'fiscal_idnum',
            'grade',
            'status',

        ]