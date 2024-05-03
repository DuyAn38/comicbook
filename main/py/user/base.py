from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category
from main.models import comic
from main.models import *
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage


def base(request):
    categories = category.objects.filter(is_sub=False)

    comics = comic.objects.all()
    print(comics)

    context = {
        'comics': comics,
        'categories': categories,
    }
    return render(request, 'user/base.html', context)


def home(request):
    latest_comics = comic.objects.order_by('-id')[:15]
    top_comics = comic.objects.order_by('-view')[:5]
    comics = comic.objects.all()
    categories = category.objects.filter(is_sub=False)
    
    context = {
        'comics': comics,
        'top_comics': top_comics,
        'latest_comics': latest_comics,
        'categories': categories,
    }
    return render(request, 'user/home.html', context)


def home(request):
    latest_comics = comic.objects.order_by('-id')[:15]  # Lấy ra 15 truyện mới nhất theo id giảm dần
    top_comics = comic.objects.order_by('-view')[:5]
    all_comics = comic.objects.all()
    paginator = Paginator(all_comics, 15)
    page_number = request.GET.get('page', 1)

    try:
        comics = paginator.page(page_number)
    except EmptyPage:
        comics = paginator.page(paginator.num_pages)

    categories = category.objects.filter(is_sub=False)

    context = {
        'comics': comics,
        'top_comics': top_comics,
        'latest_comics': latest_comics,
        'categories': categories,
    }
    return render(request, 'user/home.html', context)

