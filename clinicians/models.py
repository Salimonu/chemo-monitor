import uuid

from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from core.utils.dates import calculate_age
from core.models import GenderChoices


class ClinicianVerification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='clinician_verification')
    hospital = models.CharField(max_length=100, blank=True)
    registration_number = models.CharField(max_length=50, unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    license_expiration_date = models.DateField()
    current_license = models.ImageField(upload_to='clinician_licenses/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Clinician Verification'
    
    def __str__(self):
        return f'{self.user.username} - {self.created_at}'


class Clinician(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='clinician')
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='clinician_profiles/', default='images/default-clinician.jpeg', null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=15, choices=GenderChoices.choices, default=GenderChoices.MALE)
    date_of_birth = models.DateField()
    specialty = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    # verification_requested = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_complete = models.BooleanField(default=False)
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

    # def __str__(self):
    #     return f'{self.full_name} - {self.specialty}'
    
    def __str__(self):
        return f'{self.user.username} - {self.specialty}'
    