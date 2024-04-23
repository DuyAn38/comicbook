from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category


def search(requert):
    return render(requert,'user/search.html')