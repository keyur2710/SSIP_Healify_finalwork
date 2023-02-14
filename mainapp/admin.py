from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Doctor)
admin.site.register(models.Depressiontest)
admin.site.register(models.Diseasetest)
admin.site.register(models.Desease)
admin.site.register(models.Userprofile)
admin.site.register(models.PatientDoctorConnect)
admin.site.register(models.Newtest)

