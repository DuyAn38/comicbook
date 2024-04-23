from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *

def chapadmin(requert):
    return render(requert,'admin/chapadmin.html')
