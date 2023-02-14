from unicodedata import name
from django.contrib import admin
from django.urls import  path
from mainapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("doctors",views.doctor_list, name ='doctor_list'),
    path("getdoctor",views.get_doctor,name='getdoctorss'),
    path("test",views.Depressiontest_list, name='test'),
    path("signup",views.Signup,name = 'signup'),
    path("signin",views.Signin,name= 'signin'),
    path("gettest",views.get_test,name='gettest'),
    path("deseasetest",views.Deseasetest_list,name='deseasetest'),
    path("get_disease",views.get_disease,name='get_disease'),
    path("userprofile",views.get_Userprifile,name='userprofile'),
    path("doctorappointmentrequest",views.get_doctorappointment,name='appointment'),
    path("acceptappointment",views.accept_patieontappointment,name='approveappointment'),
    path("viewappointmentrequest",views.view_appointmentRequest,name='abcsd'),
    path("viewactivepatieont",views.active_patieont,name='abc'),
    path("deniedpatieontrequest",views.denied_patieontappointment,name='assdf'),
    path("getuser",views.get_user,name='ssdddf'),
    path("viewpendingReqByuser",views.pending_reqfromuser,name='ssdsasw'),
    path("viewactiveReqByuser",views.active_reqfromuser,name='abc'),
    path("Newtest",views.Newtest_list,name='ddffgg'),
    path("getNewtest",views.get_Newtest,name='sdsdsds'),
    path("getNewtestMap",views.Newtest_listmap,name='sdsdasdsadaa'),
    
]