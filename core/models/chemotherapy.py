from django.db import models


class ChemotherapyRegimenName(models.Model):
    """This represents different types of chemotherapy regimens."""

    # name eg EC
    name = models.CharField(max_length=100, unique=True)
    # description eg 'Epirubicin + Cyclophosphamide'
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Chemotherapy regimens'

    def __str__(self):
        return self.name
