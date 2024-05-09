from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import JsonResponse

#member
from .py.user.base import base,home
from .py.user.account import information,register,login_view,logout_view,changepassword
from .py.user.categoryuser import categoryuser
from .py.user.search import search
from .py.user.readcomic import readcomic
from .py.user.detai import detai
from .py.user.follow import comic_follow,followcomic,unfollowcomic

#admin
from .py.admin.baseadmin import baseadmin
from .py.admin.categoryadmin import categoryadmin, add_category, edit_category,delete_category
from .py.admin.comicadmin import comicadmin, add_comic, edit_comic, delete_comic
from .py.admin.useradmin import useradmin, add_user, edit_user, delete_user
from .py.admin.chapadmin import chapadmin, add_chap, edit_chap, delete_chap

import urllib.request