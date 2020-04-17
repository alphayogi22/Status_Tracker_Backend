from krasheet.models import Krasheet
from rest_framework import viewsets, permissions
from .serializers import KrasheetSerializer


# Lead Viewset
class KrasheetViewset(viewsets.ModelViewSet):
    queryset = Krasheet.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = KrasheetSerializer
