from django.db.models.signals import post_save
from django.dispatch import receiver
from inscriptions.models import Inscription
from students.models import Student
from enrollments.models import Enrollment

@receiver(post_save, sender=Inscription)
def approved_inscriptions(sender, instance, created, **kwargs):
    if instance.status == "approved":
        student, _ = Student.objects.get_or_create(
            full_name=instance.full_name,
            date_of_birth=instance.date_of_birth,
            idnumber=instance.idnumber,
            phone_number=instance.phone_number,
            grade=instance.grade
        )
        enrollment, _ = Enrollment.objects.get_or_create (student=student,)
