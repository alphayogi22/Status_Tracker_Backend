from rest_framework import serializers
from dailyusers.models import StatusTrackerUser


class DailyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTrackerUser
        fields = ['id', 'email', 'department', 'band', 'team', 'leavebalance']
