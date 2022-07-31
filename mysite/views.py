from django.shortcuts import render
from django.contrib import messages
from django.db import models
from django.shortcuts import render,redirect
from mysite.models import Tregister, Sregister
from django.contrib.auth import get_user_model
User=get_user_model()
# views take the Http requests and returns http response
from django.contrib.auth import authenticate, login
def index(request):
    return render(request,"index.html")
def sprofile(request):
    return render(request,"sprofile.html")
def tprofile(request):
    return render(request,"tprofile.html")

def slogin(request):# login for student with name password
    if request.method=="POST":
        sname=request.POST.get('sname')
        pass1=request.POST.get('pass1')
        user=authenticate(username=sname,password=pass1)
        if user is not None and user.is_student:
            login(request,user)
            messages.success(request,"successfully logged in")
            return render(request,"sprofile.html")
        else:
            messages.error(request,"invalid credentials")
            return redirect("slogin")
    return render(request,"slogin.html")
def tlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None and user.is_recruiter:
            login(request,user)
            messages.info(request,"successfully logged in")
            return render(request,"tprofile.html")
        else:
            messages.error(request,"invalid credentials")
            return redirect("tlogin")
    return render(request,"tlogin.html")
def tregister(request): # registration for teachers
    if request.method=="POST":
        username=request.POST.get('username')
        subject=request.POST.get('subject')
        ctaught=request.POST.get('ctaught')
        idno=request.POST.get('idno')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        Rpassword=request.POST.get('Rpassword')
        myuser=Tregister(username=username,subject=subject,ctaught=ctaught,idno=idno,contact=contact,password=password)
        myuser.save()
        en=User.objects.create_user(username=username,password=password)
        en.first_name=username
        en.last_name=idno
        en.save()
        messages.success(request,"successfully registered....")
        return redirect('tregister')
    return render(request,"tregister.html")
def sregister(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        rollno=request.POST.get('rollno')
        standard=request.POST.get('standard')
        stream=request.POST.get('stream')
        pass1=request.POST.get('pass1')
        myuser=Sregister(sname=sname,rollno=rollno,standard=standard,stream=stream,pass1=pass1)
        myuser.save()
        en=User.objects.create_user(username=sname,password=pass1)
        en.first_name=sname
        en.last_name=rollno
        en.save()
        messages.success(request,"successfully registered....")
        return redirect('/slogin')
    return render(request,"sregister.html")