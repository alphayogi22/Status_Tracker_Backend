from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import StatusTrackerUserManager


class StatusTrackerUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StatusTrackerUserManager()
    department = models.CharField(blank=True, max_length=250)
    band = models.CharField(blank=True, max_length=10)
    team = models.CharField(blank=True, max_length=250)
    leavebalance = models.IntegerField(null=True)
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
