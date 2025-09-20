from rest_framework import generics, permissions
from api.models import Consultation
from api.serializers import ConsultationSerializer

class ConsultationListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        return Consultation.objects.all()

class ConsultationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.all()
