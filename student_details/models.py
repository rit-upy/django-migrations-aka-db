from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Student(models.Model):

    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    marks = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    

    def __str__(self):

        return f'{self.student_id} {self.name}. {str(self.marks)}'
