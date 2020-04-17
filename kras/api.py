from kras.models import Kra
from rest_framework import viewsets, permissions
from .serializers import KraSerializer


# Lead Viewset
class KraViewset(viewsets.ModelViewSet):
    queryset = Kra.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = KraSerializer
