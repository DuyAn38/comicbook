from django.shortcuts import render
from django.db.models import Q
from main.models import *


def search(request):
    categories = category.objects.filter(is_sub=False)
    key = request.GET.get("key_word")
    list_search = comic.objects.none()

    if key:
        list_search = comic.objects.filter(Q(name__icontains=key))

    context = {
        "key": key,
        "list_search": list_search,
        "categories" : categories,
    }
    return render(request, "user/search.html", context)