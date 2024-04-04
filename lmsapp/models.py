from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    programe=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    regdate=models.CharField(max_length=30)

    

class Login(models.Model):
    userid=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=5)

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=20)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)






    