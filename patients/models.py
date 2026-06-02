import uuid

from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

from clinicians.models import Clinician
from core.utils import calculate_age, calculate_bmi
from core.models import GenderChoices, BloodGroupChoices, SeverityChoices, AllergyReaction, AllergySubstance, CancerType, CancerStage


class Patient(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hospital_id = models.CharField(max_length=20, unique=True)
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='patientS')
    managing_consultant = models.ForeignKey(Clinician, on_delete=models.PROTECT, related_name='patients')
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='patient_profiles/', default='images/default-patient.jpg', null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    emergency_contact = PhoneNumberField(null=True, blank=True)
    home_address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GenderChoices.choices, default=GenderChoices.FEMALE)
    weight = models.DecimalField(max_digits=3, decimal_places=1, help_text="Weight in KG", null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, help_text="Height in CM", null=True, blank=True)
    allergies = models.ManyToManyField(AllergySubstance, through='PatientAllergy', related_name='patients')
    cancer = models.ManyToManyField(CancerType, through='PatientCancer', related_name='patients')
    next_of_kin_name = models.CharField(max_length=50)
    next_of_kin_relationship = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, choices=BloodGroupChoices.choices, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    def __str__(self):
        return f'{self.surname} {self.first_name} - {self.hospital_id}' 

    @property
    def age(self):
        return calculate_age(self.date_of_birth)

    @property
    def bmi(self):
        return calculate_bmi(self.weight, self.height)    
    

class PatientAllergy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_allergies')
    allergy_substance = models.ForeignKey(AllergySubstance, on_delete=models.PROTECT, related_name='patient_allergies')
    reaction = models.ForeignKey(AllergyReaction, on_delete=models.PROTECT)
    severity = models.CharField(max_length=50, choices=SeverityChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('patient', 'allergy_substance')

    def __str__(self):
        return f'{self.patient.surname} {self.patient.first_name} - {self.allergy_substance.name}'
    

class PatientCancer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_cancers')
    cancer_type = models.ForeignKey(CancerType, on_delete=models.PROTECT, related_name='patient_cancers')
    cancer_stage = models.IntegerField(choices=CancerStage.choices)
    on_chemotherapy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.surname} {self.patient.first_name} - {self.cancer_type.name}'
