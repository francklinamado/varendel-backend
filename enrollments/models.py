from django.db import models
from students.models import Student

# Create your models here.
class Enrollment (models.Model):
    student = models.OneToOneField (Student, on_delete=models.CASCADE )
    #course = 
    #start_date = 
    #end_date =  
    #status = 
    #grade =
    #payment
    date_enrolled = models.DateTimeField (auto_now_add=True, null=False)

    def __str__(self):
        return f'{self.full_name}'