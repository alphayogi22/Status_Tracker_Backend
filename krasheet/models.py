from django.db import models

# Create your models here.
from kras.models import Kra


class Krasheet(models.Model):
    kra = models.ForeignKey(Kra, on_delete=models.CASCADE)
    Responsibility = models.CharField(max_length=500)
    percentageWeight = models.IntegerField(null=True)
    percentageAchieved = models.IntegerField(null=True)
    successMeasured = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    remarks = models.CharField(max_length=250)
    threshold = models.BooleanField()
    developmentGoal = models.BooleanField()
    gestalt = models.BooleanField()
