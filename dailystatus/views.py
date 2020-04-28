from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Dailystatus
from .serializers import DailystatusSerializer


class DailyStatusViewSet(GenericViewSet,  # generic view functionality
                         CreateModelMixin,  # handles POSTs
                         RetrieveModelMixin,  # handles GETs for 1 Users
                         UpdateModelMixin,  # handles PUTs and PATCHES Users
                         ListModelMixin,  # handles GETs for many Users
                         DestroyModelMixin):  # handles DELETE User):

    serializer_class = DailystatusSerializer
    queryset = Dailystatus.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user', 'status']

    def get_queryset(self):
        start_date = self.request.query_params.get('startDate', None)
        end_date = self.request.query_params.get('endDate', None)
        if start_date is not None and end_date is not None:
            return Dailystatus.objects.filter(startDate__gte=start_date, endDate__lte=end_date)
