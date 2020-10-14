from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Certificates

# Create your views here.
class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ('id','name','description','created_at', 'updated_at') 
    
    
class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
