from django.db import models
from .patient import Patient
from .doctor import Doctor
from .nurse import Nurse
from django.utils import timezone

class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='vitals')
    recorded_by_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    recorded_by_nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    # Vital measurements
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    oxygen_saturation = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    # Status for workflow
    reviewed_by_doctor = models.BooleanField(default=False)  # doctor marks after review

    def __str__(self):
        return f"Vitals for {self.patient} on {self.date}"
