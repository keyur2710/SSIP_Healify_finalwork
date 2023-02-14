from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language_choice = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Gujrati', 'Gujrati'),
    ]
    language = models.CharField( max_length=20,choices=language_choice,default='English')
    expertise = models.CharField(max_length=100)
    fee = models.IntegerField()
    name = models.CharField(max_length=100)
    year_of_expierence = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=100)
    license = models.IntegerField()
    proefficiency = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name

# ---------------------------------------------------------------------------
class Depressiontest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    above_30_age = models.IntegerField()
    city = models.IntegerField()
    sadness_momentarily = models.IntegerField()
    time_of_day = models.IntegerField()
    changes_in_life = models.IntegerField()
    activities = models.IntegerField()
    supported = models.IntegerField()
    mean_something = models.IntegerField()
    mental_health_condition = models.IntegerField()
    leave = models.IntegerField()
    substance_abuse = models.IntegerField()
    therepy = models.IntegerField()
    concentrating = models.IntegerField()
    prediction = models.IntegerField()
    
    def __int__(self):
        return 
    
# -------------------------------------------------------------------------
class Diseasetest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numbness = models.IntegerField()
    headache = models.IntegerField()
    vision_changes = models.IntegerField()
    breathing = models.IntegerField()
    heart_rate = models.IntegerField()
    body_sweating = models.IntegerField()
    thought = models.IntegerField()
    weight = models.IntegerField()
    feeling = models.IntegerField()
    frustrated = models.IntegerField()
    nightmares = models.IntegerField()
    traumetic = models.IntegerField()
    shouted_fight = models.IntegerField()
    social = models.IntegerField()
    hyper = models.IntegerField()
    prediction = models.IntegerField()
    percentage = models.IntegerField()

# --------------------------------------------------------------------------------------
class Desease(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
        

# -----------------------------------------------------------------

class Userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    weight = models.IntegerField()
    gender = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

# =============================================================
class PatientDoctorConnect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    accepted = models.BooleanField()


class Newtest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Age = models.IntegerField()
    Gender = models.IntegerField()
    self_employed = models.IntegerField()
    family_history = models.IntegerField()
    work_interfere = models.IntegerField()
    no_employees = models.IntegerField()
    remote_work = models.IntegerField()
    tech_company = models.IntegerField()
    benefits = models.IntegerField()
    care_options = models.IntegerField()
    wellness_program = models.IntegerField()
    seek_help = models.IntegerField()
    anonymity = models.IntegerField()
    leave = models.IntegerField()
    mental_health_consequence = models.IntegerField()
    phys_health_consequence = models.IntegerField()
    coworkers = models.IntegerField()
    supervisor =  models.IntegerField()
    phys_health_interview = models.IntegerField()
    mental_vs_physical  = models.IntegerField()
    MentalHealthProblem = models.IntegerField()
    prediction = models.IntegerField()


