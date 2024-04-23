from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import JsonResponse

#member
from .py.user.base import base,home
from .py.user.detai import detai
from .py.user.account import information,register,login_view,logout_view,changepassword
from .py.user.categoryuser import categoryuser
from .py.user.search import search
from .py.user.readcomic import readcomic
from .py.user.follow import follow

#admin
from .py.admin.baseadmin import baseadmin,homeadmin
from .py.admin.categoryadmin import categoryadmin
from .py.admin.comicadmin import comicadmin
from .py.admin.useradmin import useradmin
from .py.admin.chapadmin import chapadmin






