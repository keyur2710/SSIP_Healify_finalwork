# from os import pread
from pickle import TRUE
import pickle
import string 
# from pickle import *
from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
#from .models import Depressiontest, Doctor
from .models import *
from .serializers import Depressiontestserializer, Doctorserializer
#from django.shortcuts import render,HttpResponse
#from django.http import JsonResponse
#from .models import Doctor
#from .serializers import Doctorserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView




# Create your views here.
def index(request):
    return HttpResponse("hell")

@parser_classes([MultiPartParser])
@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET': 
       doctors = Doctor.objects.all()
       serializer = Doctorserializer(doctors,many=True)
       return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        serializer = Doctorserializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            print("valid")
            serializer.save()
            print(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            # return Response('hell')



@api_view(['GET', 'POST'])
def get_doctor(request):
    if request.method == 'GET': 
       doctor_id= request.GET.get('id')
       user = User.objects.get(id= doctor_id)
       #doctor = Doctor.objects.get(user=user)
       doctor = Doctor.objects.get(id=doctor_id)
       serializer = Doctorserializer(doctor)
       return JsonResponse(serializer.data)


@api_view(['GET','POST'])
def Depressiontest_list(request):
    # Depressiontestes = Depressiontest.objects.all()
    # serializer1 = Depressiontestserializer(Depressiontestes,many=True)
    # return JsonResponse ({'Test' : serializer1.data} , safe=False)

    if request.method == 'POST':
        serializer1 = Depressiontestserializer(data=request.data)
        if serializer1.is_valid():
            file = open("D:\Healify\mainapp\mlworks\model.sav",'rb')
            model = pickle.load(file)
            pred = model.predict_proba([[serializer1.validated_data["above_30_age"],
            serializer1.validated_data["city"],
            serializer1.validated_data["sadness_momentarily"],
            serializer1.validated_data["time_of_day"],
            serializer1.validated_data["changes_in_life"],
            serializer1.validated_data["activities"],
            serializer1.validated_data["supported"],
            serializer1.validated_data["mean_something"],
            serializer1.validated_data["mental_health_condition"],
            serializer1.validated_data["leave"],
            serializer1.validated_data["substance_abuse"],
            serializer1.validated_data["therepy"]]])
            print(pred[0][1])
            per = pred[0][1]
            per = int(per*100)
            serializer1.validated_data["prediction"] = per
            serializer1.save()
            return Response(serializer1.data, status = status.HTTP_201_CREATED)
        else:
            data= {"Error":"Be yrr bau thayu haju Error aave che"}
            return Response(data)
            

@api_view(['GET','POST'])
def Signup(request):
    if request.method == 'POST':
        serializer1 = Signupserializer(data=request.data)
        if serializer1.is_valid():
            user = User()
            user.username = serializer1.validated_data['email']
            user.email = serializer1.validated_data['email']
            user.first_name = serializer1.validated_data['username']
            # user.last_name(serializer1.validated_data['id'])
            user.set_password(serializer1.validated_data['password'])
            user.save()
            # User.objects.get(username = serializer1.validated_data['email'])
            dictionary = {"username":user.first_name, "id":user.id, "email":user.email}
            return Response(dictionary, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def Signin(request):
    if request.method == 'POST':
        # serializer = (data=request.data, context={"request": request})
        serializer = Signinserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           email = serializer.validated_data['email']
           password = serializer.data['password']
           user = User.objects.get(email=email)
        if user.check_password(password):
            # data = {"id": user.id, "email": user.email}
            data = {"id": user.id, "email": user.email, "username":user.first_name}
            return Response(data)
        else:
            return Response({"Error": "Wrong Password"})

@api_view(['GET', 'POST'])
def get_test(request):
    if request.method == 'GET': 
       #doctor_id= request.GET.get('id')
       test_user = request.GET.get('user')
       user = User.objects.get(id=test_user)
       #doctor = Doctor.objects.get(user=user)
       #test = Depressiontest.objects.filter(user = test_user)
       test = Depressiontest.objects.filter(user = test_user)
       serializer = Depressiontestserializer(test,many=True)
       return JsonResponse(serializer.data,safe=False)


@api_view(['GET','POST'])
def Deseasetest_list(request):
    if request.method == 'POST':
        serializer2 = Deseasetestserializer(data=request.data)
        if serializer2.is_valid():
            file = open("D:\Healify\mainapp\mlworks\model2.sav",'rb')
            model = pickle.load(file)
            pred1 = model.predict([[serializer2.validated_data["numbness"],
            serializer2.validated_data["headache"],
            serializer2.validated_data["vision_changes"],
            serializer2.validated_data["breathing"],
            serializer2.validated_data["heart_rate"],
            serializer2.validated_data["body_sweating"],
            serializer2.validated_data["thought"],
            serializer2.validated_data["weight"],
            serializer2.validated_data["feeling"],
            serializer2.validated_data["frustrated"],
            serializer2.validated_data["nightmares"],
            serializer2.validated_data["traumetic"],
            serializer2.validated_data["shouted_fight"],
            serializer2.validated_data["social"],
            serializer2.validated_data["hyper"]]])

            
            pred2 = model.predict_proba([[serializer2.validated_data["numbness"],
            serializer2.validated_data["headache"],
            serializer2.validated_data["vision_changes"],
            serializer2.validated_data["breathing"],
            serializer2.validated_data["heart_rate"],
            serializer2.validated_data["body_sweating"],
            serializer2.validated_data["thought"],
            serializer2.validated_data["weight"],
            serializer2.validated_data["feeling"],
            serializer2.validated_data["frustrated"],
            serializer2.validated_data["nightmares"],
            serializer2.validated_data["traumetic"],
            serializer2.validated_data["shouted_fight"],
            serializer2.validated_data["social"],
            serializer2.validated_data["hyper"]]])
            print(pred1)
            # if(pred1==0):
            #     pred1=6
            per = pred2[0][pred1]
            per = int(per*100)
            print(pred2)
            if(pred1[0]==6):
                pred1[0]=7
            if(pred1[0]==0):
                pred1[0]=6
            # if(pred1[0]==0):
            #     pred1[0]=7
            # if(pred1[0]==6):
            #     pred1[0]=6
            # if(pred1[0]==6):
                # pred1[0]=7
            serializer2.validated_data["prediction"] = pred1[0]
            serializer2.validated_data["percentage"] = per
            serializer2.save()
            d = Desease.objects.get(id = pred1[0])
            dictionary1 = {"prediction":d.name, "percentage":per,"description":d.description}
            # return Response(serializer2.data, status = status.HTTP_201_CREATED)
            return Response(dictionary1, status = status.HTTP_201_CREATED)
        else:
            data= {"Error":serializer2._errors}
            return Response(data)
        


@api_view(['GET', 'POST'])
def get_disease(request):
    if request.method == 'GET': 
       #doctor_id= request.GET.get('id')
       test_user = request.GET.get('user')
       user = User.objects.get(id=test_user)
       #doctor = Doctor.objects.get(user=user)
       #test = Depressiontest.objects.filter(user = test_user)
       test = Diseasetest.objects.filter(user = test_user)
       serializer = Deseasetestserializer(test,many=True)
       return JsonResponse(serializer.data,safe=False)


@api_view(['GET','POST'])
def get_Userprifile(request):
    if request.method == 'GET':
        profile = Userprofile.objects.all()
        serializer = Userprofileserializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = Userprofileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def get_user(request):
    if request.method == 'GET':
        abc=request.GET.get('user')
        bcd = Userprofile.objects.filter(user=abc)
        serializer = Userprofileserializer(bcd, many=True)
        return JsonResponse(serializer.data,safe=False)









@api_view(['GET','POST'])
def get_doctorappointment(request):
    if request.method == 'POST':
       serializer = Doctorappointmentserializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def accept_patieontappointment(request):
    if request.method == 'POST':
       doctor = request.data['doctor']
       user = request.data['user']
    #    sql = 'select * from mainapp_patientdoctorconnect where doctor=' + doctor

       a = PatientDoctorConnect.objects.get(doctor=doctor,user=user)
       a.accepted=True
       a.save()
       print(a)
       print(a.accepted)
       dict = {"doctor":a.doctor.id,"user":a.user.id,"accepted":a.accepted}
       return Response(dict)


# @api_view(['GET','POST'])
# def view_appointmentRequest(request):
#     if request.method == 'GET':
#         profile = PatientDoctorConnect.objects.raw('select * from mainapp_patientdoctorconnect where accepted=0')
#         serializer = Doctorappointmentserializer(profile, many=True)
#         return JsonResponse(serializer.data, safe=False)

@api_view(['GET','POST'])
def view_appointmentRequest(request):
    if request.method == 'GET':
        abc = request.GET.get('user')
        print(abc)
        bcd = PatientDoctorConnect.objects.filter(accepted=0, doctor= abc)
        print(bcd)
        data = []
        for i in bcd:
            # U = User.objects.get(id=i.)
            print(i)
            d= Userprofile.objects.get(user=i.user)
            data.append(d)

        print(data)      
        serializer = Userprofileserializer(data,many=True) 
        return JsonResponse({'response':serializer.data},safe=False)



@api_view(['GET','POST'])
def active_patieont(request):
    if request.method == 'GET':
        abc = request.GET.get('user')
        print(abc)
        bcd = PatientDoctorConnect.objects.filter(accepted=1, doctor= abc)
        print(bcd)
        data = []
        for i in bcd:
            # U = User.objects.get(id=i.)
            print(i)
            # d= Userprofile.objects.get(user=i.user)
            d= Userprofile.objects.get(user=i.user)
            data.append(d)
        # serializer = Doctorappoi
        # ntmentserializer(bcd,many=True)
        # serializer1 = Doctor 
        print(data)      
        serializer = Userprofileserializer(data,many=True) 
        return JsonResponse(serializer.data,safe=False)

@api_view(['GET','POST'])
def denied_patieontappointment(request):
    if request.method == 'POST':
       doctor = request.data['doctor']
       user = request.data['user']
    #    sql = 'select * from mainapp_patientdoctorconnect where doctor=' + doctor

       a = PatientDoctorConnect.objects.filter(doctor=doctor,user=user)
       a.delete()

       return Response({"data":"record deleted"})



# @api_view(['GET','POST'])
# def count_patieont(request):
#     if request.method == 'GET':
#         abc = request.GET.get('user')
@api_view(['GET','POST'])
def pending_reqfromuser(request):
    if request.method == 'GET':
        abc = request.GET.get('user')
        bcd = PatientDoctorConnect.objects.filter(accepted=0, user=abc)
        serializer = Doctorappointmentserializer(bcd,many=True)
        return JsonResponse(serializer.data,safe=False)


@api_view(['GET','POST'])
def active_reqfromuser(request):
    if request.method == 'GET':
        abc = request.GET.get('user')
        bcd = PatientDoctorConnect.objects.filter(accepted=1, user=abc)
        serializer = Doctorappointmentserializer(bcd,many=True)
        return JsonResponse(serializer.data,safe=False)


@api_view(['GET','POST'])
def Newtest_list(request):
    if request.method == 'POST':
        serializer1 = Newtestserializer(data=request.data)
        if serializer1.is_valid():
            file = open("D:\\ssip\\Healify\\mainapp\\mlworks\\newmodel.sav",'rb')
            model = pickle.load(file)
            pred = model.predict_proba([[serializer1.validated_data["Age"],
            serializer1.validated_data["Gender"],
            serializer1.validated_data["self_employed"],
            serializer1.validated_data["family_history"],
            serializer1.validated_data["work_interfere"],
            serializer1.validated_data["no_employees"],
            serializer1.validated_data["remote_work"],
            serializer1.validated_data["tech_company"],
            serializer1.validated_data["benefits"],
            serializer1.validated_data["care_options"],
            serializer1.validated_data["wellness_program"],
            serializer1.validated_data["seek_help"],
            serializer1.validated_data["anonymity"],
            serializer1.validated_data["leave"],
            serializer1.validated_data["mental_health_consequence"],
            serializer1.validated_data["phys_health_consequence"],
            serializer1.validated_data["coworkers"],
            serializer1.validated_data["supervisor"],
            serializer1.validated_data["phys_health_interview"],
            serializer1.validated_data["mental_vs_physical"],
            serializer1.validated_data["MentalHealthProblem"],
            ]])
            print(pred[0][1])
            per = pred[0][1]
            per = int(per*100)
            serializer1.validated_data["prediction"] = per
            serializer1.save()
            return Response(serializer1.data, status = status.HTTP_201_CREATED)
        else:
            data= {"Error":"Be yrr bau thayu haju Error aave che"}
            return Response(data)



@api_view(['GET', 'POST'])
def get_Newtest(request):
    if request.method == 'GET': 
       #doctor_id= request.GET.get('id')
       test_user = request.GET.get('user')
       user = User.objects.get(id=test_user)
       #doctor = Doctor.objects.get(user=user)
       #test = Depressiontest.objects.filter(user = test_user)
       test = Newtest.objects.filter(user = test_user)
       serializer = Newtestserializer(test,many=True)
       return JsonResponse(serializer.data,safe=False)


@api_view(['GET','POST'])
def Newtest_listmap(request):
    if request.method == 'POST':
        serializer1 = Newtestmap(data=request.data)
        if serializer1.is_valid():
            file = open("D:\\ssip\\Healify\\mainapp\\mlworks\\newmodel.sav",'rb')
            model = pickle.load(file)
            pred = model.predict_proba([[serializer1.validated_data["Age"],
            convert("Gender",serializer1.validated_data["Gender"]),
            convert("self_employed",serializer1.validated_data["self_employed"]),
            convert("family_history",serializer1.validated_data["family_history"]),
            convert("work_interfere",serializer1.validated_data["work_interfere"]),
            convert("remote_work",serializer1.validated_data["remote_work"]),
            convert("no_employees",serializer1.validated_data["no_employees"]),
            convert("tech_company",serializer1.validated_data["tech_company"]),
            convert("benefits",serializer1.validated_data["benefits"]),
            convert("care_options",serializer1.validated_data["care_options"]),
            convert("wellness_program",serializer1.validated_data["wellness_program"]),
            convert("seek_help",serializer1.validated_data["seek_help"]),
            convert("anonymity",serializer1.validated_data["anonymity"]),
            convert("leave",serializer1.validated_data["leave"]),
            convert("mental_health_consequence",serializer1.validated_data["mental_health_consequence"]),
            convert("phys_health_consequence",serializer1.validated_data["phys_health_consequence"]),
            convert("coworkers",serializer1.validated_data["coworkers"]),
            convert("supervisor",serializer1.validated_data["supervisor"]),
            convert("phys_health_interview",serializer1.validated_data["phys_health_interview"]),
            convert("mental_vs_physical",serializer1.validated_data["mental_vs_physical"]),
            convert("mental_vs_physical",serializer1.validated_data["mental_vs_physical"]),
            ]])
            print(pred[0][1])
            per = pred[0][1]
            per = int(per*100)
            serializer1.validated_data["prediction"] = per
            return Response([serializer1.data], status = status.HTTP_201_CREATED)
        else:
            serializer1.validated_data["prediction"] = 0
            return Response(serializer1.data, status = status.HTTP_201_CREATED)

def convert(fname,data):
    if data==" " or data=="0":
        return 0
    if fname == "care_options":
        if data == "no":
            return 0
        if data == "not sure":
            return 1
        if data == "yes":
            return 2
    if fname == "benefits" or fname=="wellness_program" or fname=="seek_help" or fname=="anonymity" or fname=="MentalHealthProblem" or fname=="mental_vs_physical" :
        if data == "don't know":
            return 0
        if data == "no":
            return 1
        if data == "yes":
            return 2
    if data == "yes":
        return 1
    if data == "no":
        return 0
    if data == "male":
        return 0
    if data == "female":
        return 1
    if data == "very small":
        return 0
    if data == "small":
        return 1
    if data == "medium":
        return 2
    if data == "large":
        return 3
    if data == "very large":
        return 4
    if data == "enterprise":
        return 5
    if fname == "leave":
        if data == "don't know":
            return 0
        if data == "different":
            return 1
        if data == "easy":
            return 2 
        if data == "difficult":
            return 3
    if fname == "mental_health_consequence" or fname=="phys_health_consequence" or fname == "phys_health_interview":
        if data == "maybe":
            return 0
        if data == "no":
            return 1 
        if data == "yes":
            return 2
    if fname == "coworkers" or fname == "supervisor":
        if data == "no":
            return 0
        if data == "some of them":
            return 1
        if data == "yes":
            return 2
    
    


