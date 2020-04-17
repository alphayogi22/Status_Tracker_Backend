from django.db import models

# Create your models here.
from dailyusers.models import StatusTrackerUser


class Dailytask(models.Model):
    user = models.ForeignKey(StatusTrackerUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=1000)
    fromDateTime = models.DateTimeField()
    toDateTime = models.DateTimeField()
    status = models.CharField(max_length=20)
    partOfKra = models.BooleanField()
