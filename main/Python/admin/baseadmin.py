from django.shortcuts import render
from django.core.paginator import Paginator


def baseadmin(requert):
    return render(requert,'admin/baseadmin.html')
