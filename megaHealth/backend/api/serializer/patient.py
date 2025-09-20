from rest_framework import serializers
from api.models.patient import Patient

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            'id', 'user', 'full_name', 'dob', 'sex',
            'address', 'phone', 'email', 'emergency_contact',
            'allergies', 'blood_type', 'profile_image', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'full_name']

    def get_full_name(self, obj):
        first = obj.first_name or ""
        last = obj.last_name or ""
        return f"{first} {last}".strip()
