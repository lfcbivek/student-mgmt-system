from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Waitlist
# Create your views here.
class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ('first_name','last_name', 'email', 'notes','created_at','updated_at')
        
        
class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer