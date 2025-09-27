from django.db import models
from django.utils import timezone
from .patient import Patient
from .doctor import Doctor
from .nurse import Nurse

class VitalSign(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='vital_signs'
    )
    recorded_by_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vital_signs_recorded_doctor'
    )
    recorded_by_nurse = models.ForeignKey(
        Nurse,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vital_signs_recorded_nurse'
    )
    date = models.DateTimeField(default=timezone.now)

    # Vital measurements
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    oxygen_saturation = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    # Workflow & status
    reviewed_by_doctor = models.BooleanField(default=False)  # Doctor review status
    reviewed_at = models.DateTimeField(blank=True, null=True)  # Timestamp when reviewed
    nurse_submitted = models.BooleanField(default=False)  # Did nurse submit
    doctor_submitted = models.BooleanField(default=False)  # Did doctor submit

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Vitals for {self.patient} on {self.date.strftime('%Y-%m-%d %H:%M')}"
