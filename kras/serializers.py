from rest_framework import serializers
from kras.models import Kra


class KraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kra
        fields = '__all__'
