from dailyusers.models import StatusTrackerUser
from rest_framework import viewsets, permissions
from .serializers import DailyuserSerializer


# Lead Viewset
class DailyuserViewSet(viewsets.ModelViewSet):
    queryset = StatusTrackerUser.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DailyuserSerializer
