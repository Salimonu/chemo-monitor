import uuid

from django.db import models

from clinicians.models import Clinician
from patients.models import Patient
from symptoms.models import SymptomReport


class Consultation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clinician = models.ForeignKey(Clinician, on_delete=models.PROTECT, related_name='consultations')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='consultations')
    symptom_report = models.ForeignKey(SymptomReport, on_delete=models.PROTECT, related_name='consultations')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        max_length = 50

        if len(self.message) > max_length:
            return f"{self.message[:max_length]}..."

        return self.message
