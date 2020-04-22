from dailystatus.models import Dailystatus
from rest_framework import viewsets
from .serializers import DailystatusSerializer


# Lead Viewset
class DailystatusViewset(viewsets.ModelViewSet):
    queryset = Dailystatus.objects.all()
    serializer_class = DailystatusSerializer
