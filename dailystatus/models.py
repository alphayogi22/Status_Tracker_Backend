from django.db import models

# Create your models here.
from dailyusers.models import StatusTrackerUser


class Dailystatus(models.Model):
    user = models.ForeignKey(StatusTrackerUser, on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=50)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    remark = models.CharField(blank=True, max_length=250)
