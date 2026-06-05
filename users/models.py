import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import RoleChoices


class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=RoleChoices.choices, default='patient')
    verification_requested = models.BooleanField(default=False)
    is_verified_clinician = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    