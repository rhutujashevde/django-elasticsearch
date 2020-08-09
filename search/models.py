from django.conf import settings
from django.db import models
from django.utils import timezone


class University(models.Model):
    alpha_two_code = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    domain = models.CharField(max_length=2)
    name = models.CharField(max_length=2)
    web_page = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name