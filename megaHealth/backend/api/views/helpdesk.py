# views/helpdesk.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.helpdesk_serializer import HelpDeskSerializer
from .models import HelpDesk

class HelpDeskView(APIView):
    """
    Handle patient check-ins and helpdesk actions:
    - Create new patient if needed
    - Assign doctor and appointment
    - Log action taken by operator
    """

    def get(self, request, pk=None):
        """Retrieve all helpdesk records or a single record by pk"""
        if pk:
            try:
                record = HelpDesk.objects.get(pk=pk)
            except HelpDesk.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = HelpDeskSerializer(record)
        else:
            records = HelpDesk.objects.all()
            serializer = HelpDeskSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new helpdesk record with optional patient and appointment"""
        serializer = HelpDeskSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save(operator=request.user)
            return Response(HelpDeskSerializer(record).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
