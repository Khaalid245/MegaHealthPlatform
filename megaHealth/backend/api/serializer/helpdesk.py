# serializers/helpdesk_serializer.py
from rest_framework import serializers
from .models import HelpDesk
from .patient import Patient
from .appointment import Appointment
from .doctor import Doctor

class HelpDeskSerializer(serializers.ModelSerializer):
    # Nested data for creating/fetching patient and appointment
    patient_id = serializers.IntegerField(required=False)
    doctor_id = serializers.IntegerField(required=False)
    appointment_type = serializers.ChoiceField(
        choices=[("InPerson", "In-Person"), ("Online", "Online")],
        default="InPerson",
        required=False
    )
    appointment_date = serializers.DateTimeField(required=False)
    action_taken = serializers.CharField(max_length=200)

    class Meta:
        model = HelpDesk
        fields = [
            'id', 'operator', 'patient', 'patient_id', 'doctor_id', 
            'appointment', 'appointment_type', 'appointment_date', 'action_taken', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        operator = validated_data.get('operator')
        patient_id = validated_data.pop('patient_id', None)
        doctor_id = validated_data.pop('doctor_id', None)
        appointment_date = validated_data.pop('appointment_date', None)
        appointment_type = validated_data.pop('appointment_type', 'InPerson')
        action_taken = validated_data.pop('action_taken')

        # 1️⃣ Fetch or create patient
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
        else:
            patient_data = self.initial_data.get('patient')
            patient = Patient.objects.create(**patient_data)

        # 2️⃣ Create appointment if doctor_id provided
        appointment = None
        if doctor_id:
            doctor = Doctor.objects.get(id=doctor_id)
            appointment = Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                appointment_date=appointment_date or timezone.now(),
                appointment_type=appointment_type
            )

        # 3️⃣ Create HelpDesk record
        helpdesk_record = HelpDesk.objects.create(
            operator=operator,
            patient=patient,
            appointment=appointment,
            action_taken=action_taken
        )

        return helpdesk_record
