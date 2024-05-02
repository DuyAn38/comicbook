from django.shortcuts import render
from django.db.models import Q
from main.models import *


def search(request):
    key = request.GET.get("key_word")
    list_search = comic.objects.none()

    if key:
        list_search = comic.objects.filter(Q(name__icontains=key))

    context = {
        "key": key,
        "list_search": list_search,
    }
    return render(request, "user/search.html", context)