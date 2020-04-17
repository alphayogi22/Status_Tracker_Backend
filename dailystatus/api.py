from dailystatus.models import Dailystatus
from rest_framework import viewsets, permissions
from .serializers import DailystatusSerializer


# Lead Viewset
class DailystatusViewset(viewsets.ModelViewSet):
    queryset = Dailystatus.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DailystatusSerializer
