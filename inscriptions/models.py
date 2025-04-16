from django.db import models
from students.personbase import PersonBase
from django.core.validators import MinValueValidator, MaxValueValidator

STATUS_CHOICE = [('pending','pendente'), ('approved','aprovado'), ('rejected','rejeitado') ]

class Inscription (PersonBase):
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    grade = models.IntegerField (validators= [MinValueValidator(1), MaxValueValidator(13)], null = False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"
