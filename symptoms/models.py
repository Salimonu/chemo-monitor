import uuid

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from patients.models import Patient
from chemotherapy.models import ChemotherapyCycle
from core.models import SeverityChoices, Symptoms


class SymptomReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    chemotherapy_cycle_number = models.ForeignKey(ChemotherapyCycle, on_delete=models.SET_NULL, null=True, related_name='symptom_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'symptoms reports'

    def __str__(self):
        return self.patient


class SymptomsEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='symptom_entry')
    symptom = models.ForeignKey(Symptoms, on_delete=models.PROTECT, related_name='symptom_entry')
    symptom_report = models.ForeignKey(SymptomReport, on_delete=models.PROTECT, related_name='symptom_entry')
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

    class Meta:
        verbose_name_plural = 'symptom entries'

    def __str__(self):
        return self.symptom.name
