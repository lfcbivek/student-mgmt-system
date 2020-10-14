from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Lecture

# Create your views here.
class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('title','lecturer_name','description','slides_url','duration','date','is_required') 
    
    
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
