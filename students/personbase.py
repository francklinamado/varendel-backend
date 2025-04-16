from django.db import models

class PersonBase(models.Model):
    full_name = models.CharField(max_length=40, null=False)
    date_of_birth = models.DateTimeField(null=False)
    idnumber = models.CharField (max_length=40, null=False)
    phone_number = models.IntegerField (null=False)
    email_adress = models.EmailField(max_length=254, unique=True, null=False, default = "default@gmail.com")
    fiscal_idnum = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField (auto_now_add=True)
    

    class Meta:
        abstract = True