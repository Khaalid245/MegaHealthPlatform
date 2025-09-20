from rest_framework import generics, permissions
from api.models import Prescription
from api.serializers import PrescriptionSerializer

class PrescriptionListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        return Prescription.objects.all()

class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()
