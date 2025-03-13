from django.db import models

class PessoaBase(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()

    class Meta:
        abstract = True


class Guardian(PessoaBase):
    fiscal_idnum = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} {self.fiscal_idnum}'


class Student(PessoaBase):
    grade = models.IntegerField()
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, null=True, related_name= "students")  # A chave estrangeira agora está no Student

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'



   

     
    
    