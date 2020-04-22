from kras.models import Kra
from rest_framework import viewsets
from .serializers import KraSerializer


# Lead Viewset
class KraViewset(viewsets.ModelViewSet):
    queryset = Kra.objects.all()
    serializer_class = KraSerializer
