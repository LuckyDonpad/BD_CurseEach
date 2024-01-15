import django.db.models
from django.db import models


# Create your models here.

class Test_DB(django.db.models.Model):
    content = models.CharField(max_length=128, null=True, blank=True)
