from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *

def categoryadmin(request):
    categories = category.objects.filter(is_sub=False)
    context = {
        'categories': categories,  
    }
    return render(request, 'admin/categoryadmin.html', context)
    
