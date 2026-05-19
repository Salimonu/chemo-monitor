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
