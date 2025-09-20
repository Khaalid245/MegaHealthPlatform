from rest_framework import generics, permissions
from api.models import Nurse
from api.serializers import NurseSerializer

class NurseListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NurseSerializer

    def get_queryset(self):
        return Nurse.objects.all()

class NurseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NurseSerializer
    queryset = Nurse.objects.all()
