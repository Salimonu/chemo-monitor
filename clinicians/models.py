import uuid

from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from core.utils.dates import calculate_age
from core.models import GenderChoices

class ClinicianProfile(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clinician = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='patient_profiles/', default='default/default-clinician.jpeg', null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    gender = models.CharField(max_length=15, default='male', choices=GenderChoices.choices)
    date_of_birth = models.DateField()
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.surname} {self.first_name} - {self.department}'
    
    @property
    def age(self):
        return calculate_age(self.date_of_birth)    
