from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inscription, Student, Enrollment

@receiver (post_save, sender= Inscription)

def do_enrollment (sender, instance,created,**kwargs):
    if instance.status == "approved":
       Enrollment.objects.get_or_create (student = instance.student, defaults= {
           "name": Enrollment.objects.full_name,
       })