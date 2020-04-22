from krasheet.models import Krasheet
from rest_framework import viewsets
from .serializers import KrasheetSerializer


# Lead Viewset
class KrasheetViewset(viewsets.ModelViewSet):
    queryset = Krasheet.objects.all()
    serializer_class = KrasheetSerializer
