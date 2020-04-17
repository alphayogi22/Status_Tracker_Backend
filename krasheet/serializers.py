from rest_framework import serializers
from krasheet.models import Krasheet


class KrasheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krasheet
        fields = '__all__'
