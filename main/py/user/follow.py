import re
from django.shortcuts import get_object_or_404, redirect
from main.models import *
from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse
from main.models import comic, Follow



def comic_follow(request):
    followed_comics = [] 
    if request.user.is_authenticated:
        follows = Follow.objects.filter(user=request.user)
        print('Following')
        for follow in follows:
            followed_comics.append(follow.comic)  # Thay đổi từ follow.story sang follow.comic

    for comics in followed_comics:
        latest_chapter = comics.chapters.order_by('-name').first()
        if latest_chapter:
            match = re.search(r'\d+', latest_chapter.name)
            if match:
                chapter_number = match.group() 
                comics.chapter_number = chapter_number
                comics.latest_chapter_date = latest_chapter.date 
                comics.chapter_id = latest_chapter.id
                print("Chapter number:", comics.chapter_number )
                print("Chapter id: ", comics.chapter_id)
                print("Latest chapter date:", latest_chapter.date)
            else:
                print("No number found in chapter name")
        else:
            print("No chapters found for story:", comics.name)

    context = {
        'comics': followed_comics,
    }
    return render(request, 'user/follow.html', context)
    # if request.user.is_authenticated:
    #     story = get_object_or_404(Story, id=story_id)
    #     follow, created = Follow.objects.get_or_create(user=request.user, story=story)
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


   

