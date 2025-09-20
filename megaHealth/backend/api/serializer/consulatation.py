from rest_framework import serializers
from api.models.consultation import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = [
            'id', 'patient', 'doctor', 'date', 'diagnosis', 'notes'
        ]
        read_only_fields = ['id', 'date']
