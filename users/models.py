import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('clinician', 'Clinician'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return self.username
    