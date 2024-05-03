from main.models import *
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import comic, Follow 


def followcomic(request, comic_id):
    if request.user.is_authenticated:
        comic_instance = get_object_or_404(comic, id=comic_id) 
        follow, created = Follow.objects.get_or_create(user=request.user, comic=comic_instance)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def unfollowcomic(request, comic_id):
    if request.user.is_authenticated:
        comic_instance = get_object_or_404(comic, id=comic_id)  
        Follow.objects.filter(user=request.user, comic=comic_instance).delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))