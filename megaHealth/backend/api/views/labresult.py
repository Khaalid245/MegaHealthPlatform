from rest_framework import generics, permissions
from api.models import LabResult
from api.serializers import LabResultSerializer

class LabResultListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LabResultSerializer

    def get_queryset(self):
        return LabResult.objects.all()

class LabResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LabResultSerializer
    queryset = LabResult.objects.all()
