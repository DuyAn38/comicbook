from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category



def follow (requert):
    return render(requert,'user/follow.html')