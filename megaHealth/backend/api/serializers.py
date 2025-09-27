# from rest_framework import serializers
# from .models import Patient, Appointment, Consultation, Prescription, LabResult

# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = ['id','doctor','scheduled_at','status','notes']

# class PrescriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Prescription
#         fields = ['medication','dose','duration_days']

# class ConsultationSerializer(serializers.ModelSerializer):
#     prescriptions = PrescriptionSerializer(many=True, read_only=True)
#     class Meta:
#         model = Consultation
#         fields = ['date','doctor','diagnosis','notes','prescriptions']

# class LabResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabResult
#         fields = ['test_name','result','date']

# class PatientDetailSerializer(serializers.ModelSerializer):
#     appointments = AppointmentSerializer(many=True, read_only=True)
#     consultations = ConsultationSerializer(many=True, read_only=True)
#     labresults = LabResultSerializer(many=True, read_only=True)

#     class Meta:
#         model = Patient
#         fields = ['id','first_name','last_name','dob','phone','appointments','consultations','labresults']
