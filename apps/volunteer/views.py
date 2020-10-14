from django.shortcuts import render
from .models import Volunteer, VolunteerHours
# Create your views here.
from rest_framework import serializers, viewsets

class VolunteerSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    class Meta:
        model = Volunteer
        fields = ('first_name','last_name','full_name','email','hours_available')
        

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    
    
class VolunteerHoursSerializer(serializers.ModelSerializer):
    volunteer_name = serializers.PrimaryKeyRelatedField(read_only= True)
    
    class Meta:
        model = VolunteerHours
        fields = ('volunteer','start','end','volunteer_name')
        
class VolunteerHoursViewSet(viewsets.ModelViewSet):
    queryset = VolunteerHours.objects.all()
    serializer_class = VolunteerHoursSerializer


