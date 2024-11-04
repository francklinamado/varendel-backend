from .models import Student, Guardian
from rest_framework import serializers

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth'
        ]

class GuardianSerializer (serializers.ModelSerializer):

    class Meta:
        model = Student
        Fieds = [
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'fiscal_idnum'
        ]


