from django.db import models
from .patient import Patient
from .doctor import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor  = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointments')
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=30, default='scheduled')
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-scheduled_at']

    def __str__(self):
        return f"{self.patient} - {self.scheduled_at}"
