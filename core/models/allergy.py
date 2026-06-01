from django.db import models


class AllergyCategory(models.Model):
    """This represents what the patient is allergic to"""
    
    # Drug, Food, Environment, Biologic, Latex, Insect
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True,  blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Allergy Categories'

    def __str__(self):
        return self.name
    

class AllergySubstance(models.Model):
    """This represents the allergens patient reacts to"""

    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(AllergyCategory, on_delete=models.PROTECT, related_name='substances')
    snomed_code = models.CharField(max_length=50, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Allergy substances'

    def __str__(self):
        return self.name
    

class AllergyReaction(models.Model):
    """This represents how the patient reacts to allergens."""

    name = models.CharField(max_length=100, unique=True)
    snomed_code = models.CharField(max_length=50, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Allergy Reactions'

    def __str__(self):
        return self.name
    