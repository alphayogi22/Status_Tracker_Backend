from django.db import models

# Create your models here.
from dailyusers.models import StatusTrackerUser


class Kra(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(StatusTrackerUser, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    percentageTotalPlanned = models.IntegerField(null=True)
    percentageTotalAchieved = models.IntegerField(null=True)
    quarter = models.CharField(blank=True, max_length=20)
    year = models.IntegerField()
    managerObservation = models.CharField(max_length=1000)
    selfObservation = models.CharField(max_length=1000)
    thresholdStatus = models.BooleanField()
