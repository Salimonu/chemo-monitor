from django.db import models

class Symptoms(models.Model):
    """This represents different types of possible adverse events."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    snomed_code = models.CharField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'symptoms'

    def __str__(self):
        return self.name