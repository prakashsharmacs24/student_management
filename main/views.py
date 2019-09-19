from django.shortcuts import render
from django.utils import timezone
from django.db.models.functions import TruncDate, ExtractYear
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
import django_filters
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer


class SchoolView(viewsets.ModelViewSet):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering_fields = ['title']
    filterset_fields = ['title']

class StudentView(viewsets.ModelViewSet):
   
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)  
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    ordering_fields = ['name']

    def get_queryset(self):
        res = super(StudentView, self).get_queryset()
        data = self.request.GET
        age = data and data.get('age')
        if age and int(data.get('age')) > 0:
            res = res.annotate(age_ann=(timezone.now().year-ExtractYear('dob') )).filter(age_ann=data.get('age'))
        return res
