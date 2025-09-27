from django.db import models
from django.utils import timezone
from .patient import Patient
from .doctor import Doctor
from .appointment import Appointment

class Consultation(models.Model):
    CONSULTATION_TYPE_CHOICES = [
        ("InPerson", "In-Person"),
        ("Online", "Online"),
    ]

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="consultations"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="consultations"
    )
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="consultations"
    )
    consultation_type = models.CharField(
        max_length=20, choices=CONSULTATION_TYPE_CHOICES, default="InPerson"
    )
    notes = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.consultation_type} Consultation for {self.patient} with Dr. {self.doctor} on {self.date.strftime('%Y-%m-%d %H:%M')}"
