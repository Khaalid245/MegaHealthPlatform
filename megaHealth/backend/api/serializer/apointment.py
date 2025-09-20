from rest_framework import serializers
from api.models.appointment import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'id', 'patient', 'doctor', 'scheduled_at',
            'status', 'notes', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
