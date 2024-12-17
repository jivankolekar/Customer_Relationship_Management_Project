
from django.shortcuts import render,redirect
from django.http import HttpResponse      # not necessary , html data display sathi

from .forms import CreateRecordForm, LoginForm, CreateUserForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .models import Employee

from django.contrib import messages
from django.utils import timezone

from django.core.mail import send_mail   # step1-mail
# Create your views here

def home(request):
    return render(request,'index.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Account Created Succesfully')
            
            return redirect('login')
        
    context = {'form':form}
    return render(request,'register.html', context=context)


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        
        form = LoginForm(request,data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, "Login in your A/c Succesfully")   # For message display after login
                return redirect('dashboard')
            
    context  = {'form':form}
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)

    messages.success(request, "Logout Succesfully")

    return redirect('login')


def dashboard(request):

    emp = Employee.objects.all()
    context ={'emp':emp}
    return render(request, 'dashboard.html', context)


def createRecord(request):
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your Record Added Successfully")

            return redirect ('dashboard')
        
    context = {'form':form}
    return render(request, 'createRecord.html', context)


def updaterecords(request,pk):
    emp = Employee.objects.get(id=pk)
    form = UpdateRecordForm(instance=emp)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Record Updated Successfuly")
            return redirect ('dashboard')
        
    context = {'form':form}
    return render(request, 'updateRecord.html', context)


def delete(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()

    messages.success(request, "Your Record Delete Successfully")
    return redirect ('dashboard')
     

def viewsrecord(request,pk):
    emp = Employee.objects.get(id=pk)

    context = {'emp':emp}
    
    return render(request, 'viewsRecord.html', context)


def index(request):
    pass


