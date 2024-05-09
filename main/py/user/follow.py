import re
from django.shortcuts import get_object_or_404, redirect
from main.models import *
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from main.models import comic, Follow



def comic_follow(request):
    categories = category.objects.filter(is_sub=False)
    if request.user.is_authenticated:
        followed_comics = Follow.objects.filter(user=request.user).select_related('comic')
        context = {
            'followed_comics': followed_comics,
            "categories" : categories,
        }
        return render(request, 'user/follow.html', context)
    else:
        return redirect('login')
    
  
def followcomic(request, comic_id):
    print("He1")
    print(comic_id)
    if request.user.is_authenticated:
        comic_instance = get_object_or_404(comic, id=comic_id) 
        follow, created = Follow.objects.get_or_create(user=request.user, comic=comic_instance)
        if not created:
            pass
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect('login')

def unfollowcomic(request, comic_id):
    if request.user.is_authenticated:
        comic_instance = get_object_or_404(comic, id=comic_id) 
        Follow.objects.filter(user=request.user, comic=comic_instance).delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


   

