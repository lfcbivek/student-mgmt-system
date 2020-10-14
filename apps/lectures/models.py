
from django.db import models
from apps.utils.models import Timestamps
# Create your models here.
class Lecture(Timestamps,models.Model):
    title = models.CharField( max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length = 100, default = '', blank = True)
    slides_url = models.CharField(max_length = 255)
    duration = models.IntegerField(help_text = 'Enter number of hours')
    date = models.DateField()
    is_required = models.BooleanField(default = True)