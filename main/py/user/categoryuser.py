from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category
from main.models import *
import re
from django.db.models import Q

def categoryuser(request):
    category_id = request.GET.get('category')
    categories = category.objects.all()
    selected_category = category.objects.get(id=category_id) if category_id else None
    comics = comic.objects.filter(categories=selected_category)
    print(comics)
    context = {
        'categories': categories,
        'comics': comics,
        'category': selected_category,  # Truyền đối tượng category vào context
    }
    return render(request, "user/categoryuser.html", context)


