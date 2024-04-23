
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import comic
from main.models import *



def comicadmin(request):
    comics = comic.objects.all()
    context = {
        'comics': comics, 
    }
    return render(request, 'admin/comicadmin.html', context)

