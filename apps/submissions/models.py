from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import Timestamps
from apps.projects.models import Projects

# Create your models here.
class StudentSubmission(Timestamps,models.Model):
    student = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    project = models.ForeignKey(Projects,  on_delete=models.DO_NOTHING)
    url = models.CharField( max_length=254)
    feedback = models.TextField()
    approved = models.BooleanField(default = False)