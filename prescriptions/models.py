import uuid

from django.db import models

from consultations.models import Consultation


class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consultation = models.ForeignKey(Consultation, on_delete=models.PROTECT, related_name='prescriptions')
    medications = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        max_length = 50

        if len(self.message) > max_length:
            return f"{self.message[:max_length]}..."

        return self.message