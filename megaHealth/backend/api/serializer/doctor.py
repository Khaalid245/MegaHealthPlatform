from rest_framework import serializers
from api.models.doctor import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = [
            'id', 'user', 'full_name', 'sex', 'address',
            'specialization', 'phone', 'email', 'profile_image', 'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'full_name']

    def get_full_name(self, obj):
        first = obj.first_name or ""
        last = obj.last_name or ""
        return f"{first} {last}".strip()
