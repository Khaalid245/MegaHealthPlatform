from rest_framework import serializers
from api.models.vitalsign import VitalSign

class VitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSign
        fields = [
            'id', 'patient', 'recorded_by_nurse', 'recorded_by_doctor', 'date',
            'blood_pressure', 'heart_rate', 'temperature', 'oxygen_saturation',
            'weight', 'notes', 'reviewed_by_doctor'
        ]
        read_only_fields = ['id', 'date', 'reviewed_by_doctor']
