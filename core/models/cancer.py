from django.db import models


class CancerType(models.Model):
    """This represents different types of cancers."""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Cancer Types'

    def __str__(self):
        return self.name
    

class CancerStage(models.IntegerChoices):
    ONE = 1, 'Stage 1'
    TWO = 2, 'Stage 2'
    THREE = 3, 'Stage 3'
    FOUR = 4, 'Stage 4'
