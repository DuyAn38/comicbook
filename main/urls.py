from django.contrib import admin
from django.urls import path, include

from . import views
from .views import *



urlpatterns = [
    #member
    path('base/',views.base,name='base'),
    path('',views.home, name='home'),
    path('categoryuser/',views.categoryuser, name = 'categoryuser'),
    path('detai/',views.detai, name='detai'),
    path('readcomic/<slug:chapter_slug>/',views.readcomic, name = "readcomic"),
    path('information/',views.information, name = "infomation"),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('search/',views.search, name = "search"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

    path('follow/', views.comic_follow, name='follow'),
    # Follow comic
    path('follow/<int:comic_id>/', views.followcomic, name='followcomic'),
    path('unfollow/<int:comic_id>/', views.unfollowcomic, name='unfollowcomic'),

    #admin
    path('baseadmin/', views.baseadmin, name = 'baseadmin'),
    #danhmuc
    path('categoryadmin/', views.categoryadmin, name = 'categoryadmin'),
    path('addCategory/', views.add_category, name = 'add_category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    #truyen
    path('comicadmin/', views.comicadmin, name = 'comicadmin'),
    path('addComic/', views.add_comic, name = 'add_comic'),
    path('edit-comic/<int:id>/', views.edit_comic, name='edit_comic'),
    path('delete-comic/<int:id>/', views.delete_comic, name='delete_comic'),
    #chap
    path('chap/', views.chapadmin, name = 'chapadmin'),
    path('addChap/', views.add_chap, name='add_chap'),
    path('edit-chap/<int:id>/', views.edit_chap, name='edit_chap'),
    path('delete-chap/<int:id>/', views.delete_chap, name='delete_chap'),
    #user
    path('user/', views.useradmin, name = 'useradmin'),
    path('addUser/', views.add_user, name = 'add_user'),
    path('edit-user/<int:id>/', views.edit_user, name = 'edit_user'),
    path('delete-user/<int:id>/', views.delete_user, name = 'delete_user'),
]