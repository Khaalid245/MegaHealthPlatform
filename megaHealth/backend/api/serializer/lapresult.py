from rest_framework import serializers
from api.models.labresult import LabResult

class LabResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResult
        fields = [
            'id', 'patient', 'test_name', 'result', 'date', 'attachments'
        ]
        read_only_fields = ['id', 'date']
