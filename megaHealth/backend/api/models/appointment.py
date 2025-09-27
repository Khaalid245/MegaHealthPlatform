from django.db import models
from django.utils import timezone
from .patient import Patient
from .doctor import Doctor

class Appointment(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
        ("InPerson", "In-Person"),
        ("Online", "Online"),
    ]

    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointments"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="appointments"
    )
    appointment_date = models.DateTimeField(default=timezone.now)
    appointment_type = models.CharField(
        max_length=20, choices=APPOINTMENT_TYPE_CHOICES, default="InPerson"
    )
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Scheduled"
    )
    created_at = models.DateTimeField(default=timezone.now)

    # Flag if the consultation has been done for this appointment
    consultation_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-appointment_date']

    def __str__(self):
        return f"{self.appointment_type} Appointment: {self.patient} with Dr. {self.doctor} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"
