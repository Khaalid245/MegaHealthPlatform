from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientDetailSerializer
from django.shortcuts import get_object_or_404

class PatientDashboardView(APIView):
    def get(self, request, pk):
        qs = Patient.objects.prefetch_related(
            'appointments__doctor',
            'consultations__prescriptions',
            'labresults'
        )
        patient = get_object_or_404(qs, pk=pk)
        serializer = PatientDetailSerializer(patient, context={'request': request})
        return Response(serializer.data)
