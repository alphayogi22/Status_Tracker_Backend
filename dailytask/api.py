from dailytask.models import Dailytask
from rest_framework import viewsets, permissions
from .serializers import DailytaskSerializer


# Lead Viewset
class DailytaskViewset(viewsets.ModelViewSet):
    queryset = Dailytask.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DailytaskSerializer
