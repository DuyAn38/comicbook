from django.shortcuts import render
from django.core.paginator import Paginator


def base(requert):
    return render(requert,'user/base.html')

