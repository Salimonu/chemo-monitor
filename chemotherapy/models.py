import uuid

from django.conf import settings
from django.db import models

from patients.models import Patient
from core.models import TreatmentIntentChoices, ChemotherapyRegimenName


class ChemotherapyRegimen(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='chemotherapy_regimen')
    chemotherapy_regimen = models.ForeignKey(ChemotherapyRegimenName, on_delete=models.SET_NULL, null=True, related_name='chemotherapy_regimen')
    on_chemotherapy = models.BooleanField(default=True)
    start_date = models.DateField()
    treatment_intent = models.CharField(max_length=50, choices=TreatmentIntentChoices.choices, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chemotherapy_regimen
    

class ChemotherapyCycle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='chemotherapy_cycles')
    chemotherapy_regimen = models.ForeignKey(ChemotherapyRegimen, on_delete=models.SET_NULL, null=True, related_name='chemotherapy_cycles')
    on_chemotherapy = models.BooleanField(default=True)
    cycle_number = models.SmallIntegerField(default=1)
    adverse_event = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cycle_number
