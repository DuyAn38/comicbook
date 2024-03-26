from django.shortcuts import render

# Create your views here.
def base(requert):
    return render(requert,'user/base.html')

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