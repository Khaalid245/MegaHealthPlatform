from rest_framework import serializers
from api.models.prescription import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = [
            'id', 'consultation', 'medication', 'dose', 
            'duration_days', 'instructions'
        ]
        read_only_fields = ['id']
