import uuid

from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from core.utils.dates import calculate_age
from core.models import GenderChoices


class Clinician(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clinician = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='clinician')
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='clinician_profiles/', default='default/default-clinician.jpeg', null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GenderChoices.choices, default=GenderChoices.MALE)
    date_of_birth = models.DateField()
    license_number = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname']
        verbose_name = 'Clinician'
    
    @property
    def full_name(self):
        return f'{self.surname} {self.first_name}'
    
    @property
    def age(self):
        return calculate_age(self.date_of_birth)    

    def __str__(self):
        return f'{self.full_name} - {self.specialty}'
    