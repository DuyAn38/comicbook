from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from requests import request
from main.models import *

def readcomic(request, chapter_slug):
    global chapter

    story = comic.objects.get(slug=chapter_slug)
    chapter_slug = request.GET.get('chapter_slug')
    chapters = Chap.objects.filter(story=story)
    print(chapters)
    id = request.GET.get('chap', '') 
    print('TÌm thấy id')
    print(id)
    chapter = get_object_or_404(Chap, id=id)
    chapter.view = chapter.view + 1
    chapter.save()
    prev_chapter = chapters.filter(id__lt=chapter.id).last()
    next_chapter = chapters.filter(id__gt=chapter.id).first()

    print(chapter.name)

    images = ImagesChap.objects.filter(chap=chapter)
    context = {
        'images': images,
    }
    print(images)
    return render(request,'user/readcomic.html', context)
