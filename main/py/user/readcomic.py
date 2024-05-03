from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from requests import request
from main.models import *
from django.http import Http404

def readcomic(request, chapter_slug):
    story = get_object_or_404(comic, slug=chapter_slug)
    chapters = Chap.objects.filter(story=story)
    chapter_id = request.GET.get('chap_id')
    
    try:
        if chapter_id:
            chapter = get_object_or_404(Chap, id=chapter_id)
            chapter.view += 1
            chapter.save()
        else:
            chapter_id = request.GET.get('chap', '') 
            chapter = get_object_or_404(Chap, id=chapter_id)
    except (ValueError, Http404):
        chapter = None

    prev_chapter = chapters.filter(id__lt=chapter.id).last() if chapter else None
    next_chapter = chapters.filter(id__gt=chapter.id).first() if chapter else None
    images = ImagesChap.objects.filter(chap=chapter) if chapter else None

    context = {
        'images': images,
        'chapters': chapters,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
        'comic': story,
        'current_chapter': chapter, 
    }

    return render(request, 'user/readcomic.html', context)
