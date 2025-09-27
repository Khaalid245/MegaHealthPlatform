from django.db import models
from django.utils import timezone
from .consultation import Consultation
from .doctor import Doctor
from .patient import Patient

class Prescription(models.Model):
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='prescriptions_given'
    )
    medication = models.CharField(max_length=200)
    dose = models.CharField(max_length=100, blank=True, null=True)
    duration_days = models.IntegerField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)  # e.g., take after meals
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.medication} for {self.patient} ({self.dose})"
