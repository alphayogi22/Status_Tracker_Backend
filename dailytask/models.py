from django.db import models

# Create your models here.
from dailyusers.models import StatusTrackerUser


class Dailytask(models.Model):
    user = models.ForeignKey(StatusTrackerUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=1000)
    partOfKra = models.BooleanField(default=False)
    noOfHours = models.IntegerField(null=True)
    startTime = models.TimeField(null=True )
    endTime = models.TimeField(null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20)
    remark = models.CharField(max_length=1000, null=True)
    
