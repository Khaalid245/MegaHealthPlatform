from django.db import models
from .consultation import Consultation

class Prescription(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='prescriptions')
    medication = models.CharField(max_length=200)
    dose = models.CharField(max_length=100, blank=True)
    duration_days = models.IntegerField(null=True, blank=True)
