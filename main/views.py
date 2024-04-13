from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


from .Python.user.base import *
from .Python.user.account import *


# user
def home(requert):
    return render(requert,'user/home.html')

def category(requert):
    return render(requert,'user/category.html')

def detai(requert):
    return render(requert,'user/detai.html')

def chap(requert):
    return render(requert,'user/chap.html')

def information(requert):
    return render(requert,'user/information.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')


# admin
def baseadmin(requert):
    return render(requert,'admin/baseadmin.html')