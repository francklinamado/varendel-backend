from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from inscriptions.models import Inscription
from students.personbase import PersonBase


class Guardian(PersonBase):
   

    def __str__(self):
        return f'{self.full_name}'


class Student(PersonBase):
    grade = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(13)])
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, null=True, related_name= "students")  
    inscriptions = models.OneToOneField (Inscription, on_delete=models.CASCADE, related_name="student_inscription", null=True)
    
    def __str__(self):
        return f'{self.full_name}'



   

     
    
