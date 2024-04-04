from django.shortcuts import render,redirect, reverse
from . models import Enquiry, Login, Student 
from datetime import date 
from django.contrib import messages
from adminapp . models import Program,Branch,Year
from .smssender import sendsms
from django.core.mail import send_mail
from django.conf import settings 




# Create your views here.

# def reload(request):
#     return render(request, "reload.html")

def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request,"aboutus.html")

def registration(request): 
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        programe=request.POST['programe']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        regdate=date.today()
        usertype='student'
        status='false'
        stu=Student(rollno=rollno,name=name, fname=fname, mname=mname ,gender=gender, programe=programe, branch=branch, year=year , contactno=contactno ,emailaddress=emailaddress, regdate=regdate ,address=address )
        log=Login(userid=rollno, password=password , usertype=usertype , status=status)
        stu.save()
        log.save()
        subject='Important mail from TMBU'
        msg=f'Hello {name} your registartion is successful . And your password is {password}. Thanks for choise Tilka manjhi Bhagalpur Uniercity.'
        messages.success(request,'student Resistration is done .')
        email_from=settings.EMAIL_HOST_USER
        send_mail(subject,msg,email_from,{emailaddress})
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    return render(request,"registration.html",locals())



def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj.usertype=="student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studenthome'))
                #messages.success(request,'Welcome Student ')
            elif obj.usertype=="admin":
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:
            messages.success(request,'Invalid User ')
    return render(request,"login.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)

        enq.save()
        sendsms(contactno)
        messages.success(request,'Enquiry is submited .Thanks for send your Enqyiry')
    return render(request,"contact.html")


    