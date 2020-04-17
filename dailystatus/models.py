from django.db import models

# Create your models here.
from dailyusers.models import StatusTrackerUser


class Dailystatus(models.Model):
    user = models.ForeignKey(StatusTrackerUser, on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=10)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    remark = models.CharField(blank=True, max_length=250)
