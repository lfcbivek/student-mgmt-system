from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    url = models.CharField( max_length=254)
    level = models.IntegerField(choices = ((1,'Level One'),(2,'Level 2')),default =1)
    required = models.BooleanField(default = True)
    
    class Meta:
        verbose_name_plural = 'Projects'