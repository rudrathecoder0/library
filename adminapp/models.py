from django.db import models

# Create your models here.

class BookStore(models.Model):
    bookid=models.CharField(max_length=15,primary_key=True)
    isbnno=models.CharField(max_length=15)
    programe=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    qty=models.IntegerField()

    def __str__(self):
        return self.bookid


class IssueBook(models.Model):
    bookid=models.CharField(max_length=50)
    isbnno=models.CharField(max_length=15)
    programe=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    bookname=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)
    rollno=models.IntegerField()
    name=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    issuedate=models.CharField(max_length=30)
    duedate=models.CharField(max_length=30)
    status=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Program(models.Model):
    program=models.CharField(max_length=100)

    def __str__(self):
        return self.program

class Branch(models.Model):
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.branch

class Year(models.Model):
    year=models.CharField(max_length=100)

    def __str__(self):
        return self.year




    


