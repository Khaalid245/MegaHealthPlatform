from django.db import models
from .patient import Patient
from .doctor import Doctor
from django.utils import timezone

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    doctor  = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    diagnosis = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
