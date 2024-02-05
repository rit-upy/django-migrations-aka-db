from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=50)
    marks = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

