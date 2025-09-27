# helpdesk.py
from django.db import models
from django.utils import timezone
from .patient import Patient
from .doctor import Doctor
from .appointment import Appointment
from django.conf import settings

class HelpDesk(models.Model):
    operator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='helpdesk_actions'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='helpdesk_entries'
    )
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='helpdesk_entries'
    )
    action_taken = models.CharField(max_length=200)  # e.g., "Created account", "Assigned doctor", "Sent OTP"
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"HelpDesk: {self.patient} - {self.action_taken} by {self.operator}"
