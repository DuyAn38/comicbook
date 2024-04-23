from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *

def baseadmin(requert):
    return render(requert,'admin/baseadmin.html')

def homeadmin(requert):
    return render(requert,'admin/homeadmin.html')
