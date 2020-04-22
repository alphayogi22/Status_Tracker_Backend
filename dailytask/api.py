from dailytask.models import Dailytask
from rest_framework import viewsets
from .serializers import DailytaskSerializer


# Lead Viewset
class DailytaskViewset(viewsets.ModelViewSet):
    queryset = Dailytask.objects.all()
    serializer_class = DailytaskSerializer
