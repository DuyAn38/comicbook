from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category
from main.models import *
import re
from django.db.models import Q

def categoryuser(request):
    category_id = request.GET.get('category')
    categories = category.objects.all()
    comics = comic.objects.filter()
    comic_list = comic.objects.filter(categories=category_id)
    print(comic_list)
    context ={
          
          'categories': categories,
          'comics': comic_list,
    }
    return render(request, "user/categoryuser.html", context)

