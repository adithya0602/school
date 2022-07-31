from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):# to give the access to the student and teacher by the administrator
    is_admin=models.BooleanField('Is admin',default=False)
    is_recruiter=models.BooleanField('Is teacher',default=False)
    is_student=models.BooleanField('Is student',default=False)

# Create your models here.
class Tregister(models.Model): # Each attribute of the model represents a database field like username,fname,lname,idno,email,schoolname,password
    username=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    ctaught=models.CharField(max_length=20)
    idno=models.IntegerField()
    contact=models.IntegerField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username
class Sregister(models.Model):
    sname=models.CharField(max_length=20)
    rollno=models.CharField(max_length=20)
    standard=models.CharField(max_length=40)
    pass1=models.CharField(max_length=20)
    stream=models.CharField(max_length=40)
    def __str__(self):
        return self.sname #field name where all the attributes are present