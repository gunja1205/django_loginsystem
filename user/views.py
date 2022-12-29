from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from hashlib import sha256
from .models import Vaccination_center
from django.http import HttpResponse
#from Vaccination_center import centers 

# Create your views here.
import urllib.request
import json

def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                print("success")
                return redirect('login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        print("no post method")
    return render(request, 'register.html')
        
def login_user(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html') 

def logout_user(request):
    auth.logout(request)
    return redirect('index') 

      
def admin_login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('admin_login')
    else:
        return render(request, 'admin_login.html') 


def search(request):
    # query = request.GET['query']
    # allcenters = center.objects.all()
    # allcenters = center.objects.filter(title_icontains=query)
    # params = {'allcenters ': allcenters}
    return render(request, 'search.html') 
   