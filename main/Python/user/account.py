from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from django.core.paginator import Paginator


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
        return render(request, 'login.html')

def register(requert):
    return render(requert,'user/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')
