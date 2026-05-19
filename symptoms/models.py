import uuid

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from patients.models import PatientProfile
from chemotherapy.models import ChemotherapyCycle
from core.models import SeverityChoices

class Symptoms(models.Model):
    pass


class SymptomReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    chemotherapy_cycle_number = models.ForeignKey(ChemotherapyCycle, on_delete=models.CASCADE, related_name='symptom_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SymptomsEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptoms, on_delete=models.CASCADE)
    patient_score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    clinical_grade = models.IntegerField(
        choices=SeverityChoices.choices,
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    