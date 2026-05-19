import uuid

from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from clinicians.models import ClinicianProfile
from core.utils.dates import calculate_age
from core.models import GenderChoices


class PatientProfile(models.Model):
    
    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospital_id = models.CharField(max_length=20, unique=True)
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_profile')
    managing_consultant = models.ForeignKey(ClinicianProfile, on_delete=models.SET_NULL, null=True, related_name='patients')
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='patient_profiles/', default='default/default-patient.jpg', null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    emergency_contact = PhoneNumberField(null=True, blank=True)
    home_address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=15, default='female', choices=GenderChoices.choices)
    next_of_kin_name = models.CharField(max_length=50)
    next_of_kin_relationship = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    def __str__(self):
        return f'{self.surname} {self.first_name} - {self.hospital_id}' 

    @property
    def age(self):
        return calculate_age(self.date_of_birth)
    

class Allergy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='allergies')
    allergies = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.allergies[:20]
    

class Cancer(models.Model):
    CANCER_TYPE_CHOICES = (
        ('breast_cancer', 'Breast Cancer'),
        ('prostate_cancer', 'Prostate Cancer'),
        ('rectal_cancer', 'Rectal Cancer'),
        ('colon_cancer', 'Colon Cancer'),
        ('lung_cancer', 'Lung Cancer'),
        ('other_cancers', 'Others'),
    )
    CANCER_STAGE_CHOICES = (
        (1, 'Stage 1'),
        (2, 'Stage 2'),
        (3, 'Stage 3'),
        (4, 'Stage 4'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='cancers')
    cancer_type = models.CharField(max_length=50, choices=CANCER_TYPE_CHOICES)
    cancer_stage = models.IntegerField(choices=CANCER_STAGE_CHOICES, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cancer_type} - {self.cancer_stage}'
    