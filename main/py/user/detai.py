from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category, comic, Comment
from main.models import *
from django.http import JsonResponse


def detai(request):
    slug = request.GET.get('slug', '')
    comic_instance = comic.objects.get(slug=slug)
    comic_instance.view += 1
    comic_instance.save()
    chapters = Chap.objects.filter(story=comic_instance).order_by('-id')
    categories = category.objects.all()
    list_comment = Comment.objects.filter(story=comic_instance)
    lst_story = comic.objects.all()[:4]
    comic_view_count = comic_instance.view
    first_chapter = chapters.first() if chapters.exists() else None
    last_chapter = chapters.last() if chapters.exists() else None

    follow = ''
    if request.user.is_authenticated:
        follow = Follow.objects.filter(user=request.user, comic=comic_instance)
    context = {
        'chapters': chapters,
        'comic': comic_instance,
        'slug': slug,
        'first_chapter': first_chapter,
        'last_chapter': last_chapter,
        'list_comment': list_comment,
        'categories': categories,
        'lst_story': lst_story,
        'comic_view_count': comic_view_count,
        'follow': follow,
    }
    return render(request, 'user/detai.html', context)



