from .models import Student, Guardian
from rest_framework import serializers

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'grade',
            'guardian'
        ]

class GuardianSerializer (serializers.ModelSerializer):
    #students = serializers.HyperlinkedRelatedField (many=True, read_only=True, view_name='students-detail')

    class Meta:
        model = Guardian
        fields = [
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'fiscal_idnum',
            'students',
        ]


