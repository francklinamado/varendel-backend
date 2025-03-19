from django.db import models


class Inscription (models.Model):
    name = models.CharField (max_length=100)
    email = models.EmailField (unique = True)
    phone = models.CharField (max_length=12)
    status = models.CharField(max_length=20, choices= [
        ('pending', 'pendente'),
        ('approved', 'aprovado'),
        ('rejected', 'rejeitado'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
