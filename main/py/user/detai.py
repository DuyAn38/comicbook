from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category
from main.models import *


def detai(requert):
    categories = category.objects.filter(is_sub=False)
    
    context = {
        'categories': categories,
    }
    return render(requert, 'user/detai.html', context)
   