from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category
from main.models import comic

def base(request):
    categories = category.objects.filter(is_sub=False)
    comics = comic.objects.all()
    context = {
        'comics': comics,
        'categories': categories,
    }
    return render(request, 'user/base.html', context)


def home(requert):
    categories = category.objects.filter(is_sub=False)
    comics = comic.objects.all()
    context = {
        'comics': comics,
        'categories': categories,
    }
    return render(requert,'user/home.html', context)



