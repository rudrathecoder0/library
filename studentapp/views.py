from django.shortcuts import render,redirect 
from lmsapp.models import Student,Login
from django.views.decorators.cache import cache_control
from .models import StuResponse
from datetime import date 
from django.contrib import messages 
from adminapp.models import IssueBook



# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,"studenthome.html",{'stu':stu})
    except KeyError:
        return redirect('lmsapp:login')



def studentlogout(request):
    try:
        del request.session['rollno']
    except keyError:
        return redirect('lmsapp:login')
    return redirect('lmsapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def response(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                rollno=stu.rollno
                name=stu.name
                programe=stu.programe
                branch=stu.branch
                year=stu.year
                contactno=stu.contactno
                emailaddress=stu.emailaddress
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                responsedate=date.today()                
                sr=StuResponse(rollno=rollno,name=name,programe=programe,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,responsedate=responsedate)#this is a function callin mathod 
                sr.save()
                messages.success(request,'Response is Summited ,Thanks for your feedback/Complain . ')
            return render(request,"response.html",{'stu':stu})
    except KeyError:
        return redirect('lmsapp:login')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepassword(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                confirmpassword=request.POST['confirmpassword']
                if newpassword!=confirmpassword:
                    messages.success(request,'Newpassword and confirmpassword are not matched')
                    return render(request,"changepassword.html",{'stu':stu})
               
                try:
                    log=Login.objects.get(userid=rollno,password=oldpassword)
                    Login.objects.filter(userid=rollno).update(password=newpassword)
                    return redirect('studentapp:studentlogout')
                except:
                    messages.success(request,'oldpassword is not matchde ')
        return render(request,"changepassword.html",{'stu':stu})
    except KeyError:
        return redirect('lmsapp:login')



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudentbook(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            book=IssueBook.objects.filter(rollno=rollno)

            return render(request,"viewstudentbook.html", locals())
    except KeyError:
        return redirect('lmsapp:login')





