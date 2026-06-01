from django.db import models


class SeverityChoices(models.IntegerChoices):
    NONE = 0, "None"
    MILD = 1, "Mild"
    MODERATE = 2, "Moderate"
    SEVERE = 3, "Severe"
    VERY_SEVERE = 4, "Very Severe"


class GenderChoices(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'


class BloodGroupChoices(models.TextChoices):
    A_POSITIVE = 'A+', 'A+'
    A_NEGATIVE = 'A-', 'A-'
    B_POSITIVE = 'B+', 'B+'
    B_NEGATIVE = 'B-', 'B-'
    AB_POSITIVE = 'AB+', 'AB+'
    AB_NEGATIVE = 'AB-', 'AB-'
    O_POSITIVE = 'O+', 'O+'
    O_NEGATIVE = 'O-', 'O-'


class TreatmentIntentChoices(models.TextChoices):
    CURATIVE = 'curative', 'Curative'
    PALLIATIVE = 'palliative', 'Palliative'
    
