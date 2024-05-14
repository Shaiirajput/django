from rest_framework import serializers
from .models import Student,Resume
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields=['id','name','email','dob','state','gender','location','pimage','rdoc']