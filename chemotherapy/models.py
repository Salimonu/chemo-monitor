import uuid

from django.conf import settings
from django.db import models

from patients.models import PatientProfile

class ChemotherapyRegimen(models.Model):
    CHEMOTHERAPY_REGIMEN_CHOICES = (
        ('EC', 'Epirubicin + Cyclophosphamide'),
        ('EC_T', 'Epirubicin + Cyclophosphamide + Docetaxel'),
        ('CMF', 'Cyclophosphamide, + Methotrexate + 5-Fluorouracil (5-FU)'),
        ('FOLFOX', '5-Fluorouracil (5-FU) + Leucovorin + Oxaliplatin'),
        ('FOLFIRI', '5-Fluorouracil (5-FU) + Leucovorin + Irinotecan'),
        ('CISGEM', 'Cisplatin + Gemcitabine'),
        ('CARBOPACLI', 'Carboplatin + Paclitaxel'),
        ('ECF', 'Epirubicin + Cisplatin + 5-FU'),
        ('ECX', 'Epirubicin + Cisplatin + Capecitabine'),
        ('others', 'Others'),
    )
    TREATMENT_INTENT_CHOICES = (
        ('curative', 'Curative'),
        ('palliative', 'Palliative')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='chemotherapy_regimens')
    chemotherapy_regimen = models.CharField(max_length=50, choices=CHEMOTHERAPY_REGIMEN_CHOICES)
    is_on_active_chemotherapy = models.BooleanField(default=True)
    start_date = models.DateField()
    treatment_intent = models.CharField(max_length=50, choices=TREATMENT_INTENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chemotherapy_regimen
    

class ChemotherapyCycle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='chemotherapy_cycles')
    chemotherapy_regimen = models.ForeignKey(ChemotherapyRegimen, on_delete=models.CASCADE, related_name='chemotherapy_cycles')
    is_on_active_chemotherapy = models.BooleanField(default=True)
    cycle_number = models.IntegerField(default=1)
    adverse_event = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cycle_number
    