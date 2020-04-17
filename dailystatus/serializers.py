from rest_framework import serializers
from dailystatus.models import Dailystatus


class DailystatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailystatus
        fields = '__all__'
