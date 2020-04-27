from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import StatusTrackerUser
from .serializers import DailyuserSerializer


class DailyUserViewSet(GenericViewSet,  # generic view functionality
                       CreateModelMixin,  # handles POSTs
                       RetrieveModelMixin,  # handles GETs for 1 Users
                       UpdateModelMixin,  # handles PUTs and PATCHES Users
                       ListModelMixin,  # handles GETs for many Users
                       DestroyModelMixin):  # handles DELETE User):

    serializer_class = DailyuserSerializer
    queryset = StatusTrackerUser.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'band']
