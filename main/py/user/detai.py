from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import category, comic, Comment
from main.models import *



def detai(request):
    comics = comic.objects.all()
    slug = request.GET.get('slug', '')
    comic_instance = comic.objects.get(slug=slug)
    
    # Lấy danh sách chương và sắp xếp ngược lại theo trường id
    chapters = Chap.objects.filter(story=comic_instance).order_by('-id')
    
    categories_story = comic_instance.categories.values_list('slug', flat=True)
    categories = comic_instance.categories.all()
    list_comment = Comment.objects.filter(story=comic_instance)

    lst_story = comic.objects.all()[:4]
    
    first_chapter = chapters.first() if chapters.exists() else None
    last_chapter = chapters.last() if chapters.exists() else None

    context = {
        'chapters': chapters,
        'comic': comic_instance,
        'slug': slug,
        'first_chapter': first_chapter,
        'last_chapter': last_chapter,
        'list_comment': list_comment,
        'categories': categories,
        'lst_story': lst_story
    }                                                                                                                                       
    return render(request, 'user/detai.html', context)
