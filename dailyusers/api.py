from dailyusers.models import StatusTrackerUser
from rest_framework import viewsets
from .serializers import DailyuserSerializer


# Lead Viewset
class DailyuserViewSet(viewsets.ModelViewSet):
    queryset = StatusTrackerUser.objects.all()
   
    serializer_class = DailyuserSerializer
