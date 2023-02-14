from dataclasses import fields
from http.client import HTTPResponse
import json
import re
# from typing_extensions import Self
# from mainapp.models import Doctor,Depressiontest,Diseasetest
from mainapp.models import *
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from mainapp.models import Doctor
from pyexpat import model
from rest_framework import serializers
from mainapp.models import Doctor
from django.http import JsonResponse

class Doctorserializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','user', 'language', 'expertise', 'fee', 'name', 'year_of_expierence', 'image', 'description','license','proefficiency']



class Depressiontestserializer(serializers.ModelSerializer):
    class Meta:
        model = Depressiontest
        fields = ['id', 'user', 'above_30_age', 'city', 'sadness_momentarily', 'time_of_day', 'changes_in_life', 'activities',
        'supported', 'mean_something', 'mental_health_condition', 'leave', 'substance_abuse', 'therepy', 'concentrating', 'prediction']



class Signupserializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    # confirm_password = serializers.CharField(max_length=200)


class Signinserializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)
    password =serializers.CharField(max_length=200)



class Deseasetestserializer(serializers.ModelSerializer):
    class Meta:
        model = Diseasetest
        fields = ['id', 'user', 'numbness', 'headache', 'vision_changes', 'breathing', 'heart_rate', 'body_sweating', 'thought', 'weight',
        'feeling', 'frustrated', 'nightmares', 'traumetic', 'shouted_fight', 'social','hyper', 'prediction','percentage']

# class Deseaseserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Desease
#         fields = ['id', 'name', 'description']
class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['user','fullname','bloodgroup','weight','gender','date_of_birth','image']

class Doctorappointmentserializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorConnect
        fields = ['user','doctor','accepted']

class Newtestserializer(serializers.ModelSerializer):
    class Meta:
        model = Newtest
        fields = ['id','user','Age','Gender','self_employed','family_history','work_interfere','no_employees','remote_work','tech_company','benefits',
        'care_options','wellness_program','seek_help','anonymity','leave','mental_health_consequence','phys_health_consequence','coworkers',
        'supervisor','phys_health_interview','mental_vs_physical','MentalHealthProblem','prediction']

class Newtestmap(serializers.Serializer):
    user = serializers.IntegerField()
    Age = serializers.IntegerField()
    Gender = serializers.CharField(max_length=200)
    self_employed = serializers.CharField(max_length=200)
    family_history = serializers.CharField(max_length=200)
    work_interfere = serializers.CharField(max_length=200)
    no_employees = serializers.CharField(max_length=200)
    remote_work = serializers.CharField(max_length=200)
    tech_company = serializers.CharField(max_length=200)
    benefits = serializers.CharField(max_length=200)
    care_options = serializers.CharField(max_length=200)
    wellness_program = serializers.CharField(max_length=200)
    seek_help = serializers.CharField(max_length=200)
    anonymity = serializers.CharField(max_length=200)
    leave = serializers.CharField(max_length=200)
    mental_health_consequence = serializers.CharField(max_length=200)
    phys_health_consequence = serializers.CharField(max_length=200)
    coworkers = serializers.CharField(max_length=200)
    supervisor = serializers.CharField(max_length=200)
    phys_health_interview = serializers.CharField(max_length=200)
    mental_vs_physical = serializers.CharField(max_length=200)
    MentalHealthProblem = serializers.CharField(max_length=200)
    prediction = serializers.IntegerField()

    
    def create(self, validated_data):
        return super().create(validated_data)


