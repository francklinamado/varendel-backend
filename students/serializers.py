from .models import Student, Guardian
from rest_framework import serializers

class StudentSerializer (serializers.ModelSerializer):
    grade = serializers.IntegerField(min_value =1, max_value=13)

    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'date_of_birth',
            'idnumber',
            'phone_number',
            'email_adress',
            'fiscal_idnum',
            'grade',
            'guardian',
            'created_at'
        ]

class GuardianSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Guardian
        fields = [
            'id',
            'full_name',
            'date_of_birth',
            'idnumber',
            'phone_number',
            'email_adress',
            'fiscal_idnum',
            'students',
            'created_at',
        ]


