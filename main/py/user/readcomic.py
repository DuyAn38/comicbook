from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category

def readcomic(requert):
    return render(requert,'user/readcomic.html')