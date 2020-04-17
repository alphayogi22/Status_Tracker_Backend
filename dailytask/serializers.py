from rest_framework import serializers
from dailytask.models import Dailytask


class DailytaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailytask
        fields = '__all__'
