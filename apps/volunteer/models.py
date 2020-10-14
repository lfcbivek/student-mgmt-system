from django.db import models

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    hours_available = models.IntegerField()
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
class VolunteerHours(models.Model):
    volunteer = models.ForeignKey(Volunteer,on_delete = models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'VolunteerHours'
    