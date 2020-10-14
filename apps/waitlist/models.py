from django.db import models
from apps.utils.models import Timestamps
# Create your models here.
class Waitlist(Timestamps,models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254, unique=True , verbose_name = 'email address')
    notes = models.TextField()
    
    