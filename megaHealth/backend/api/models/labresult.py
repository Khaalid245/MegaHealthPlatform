from django.db import models
from django.utils import timezone
from .patient import Patient
from .doctor import Doctor
from .consultation import Consultation

class LabResult(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='lab_results'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lab_results'
    )
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lab_results'
    )
    test_name = models.CharField(max_length=200)
    result = models.JSONField(blank=True, null=True)  # structured result
    date = models.DateTimeField(default=timezone.now)
    attachments = models.FileField(upload_to='lab_attachments/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  # lab technician notes
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.test_name} for {self.patient} on {self.date.strftime('%Y-%m-%d')}"
