from rest_framework import serializers

from .models import School, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('school', 'user', 'name', 'dob','age','is_adult')



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'title')