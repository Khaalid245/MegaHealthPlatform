from rest_framework import generics, permissions
from api.models import VitalSign
from api.serializers import VitalSignSerializer

class VitalSignListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VitalSignSerializer

    def get_queryset(self):
        return VitalSign.objects.all()

class VitalSignDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VitalSignSerializer
    queryset = VitalSign.objects.all()
