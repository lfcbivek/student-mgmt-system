from django.db import models
from apps.utils.models import Timestamps
# Create your models here.
class Certificates(Timestamps,models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    