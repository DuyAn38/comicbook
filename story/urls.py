from django.contrib import admin
from django.urls import path
from main import views as main
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #member
    path('admin/', admin.site.urls),
    path('base/',main.base,name='base'),
    path('',main.home, name='home'),
    path('categoryuser/',main.categoryuser, name = 'categoryuser'),
    path('detai/',main.detai),
    path('readcomic/',main.readcomic, name = "readcomic"),
    path('information/',main.information, name = "infomation"),
    path('changepassword/', main.changepassword, name='changepassword'),
    path('search/',main.search, name = "search"),
    path('follow/',main.follow, name = "follow"),
    path('logout/', main.logout_view, name='logout'),
    path('login/', main.login_view, name='login'),
    path('register/', main.register, name='register'),
    

    #admin
    path('baseadmin/', main.baseadmin, name = 'baseadmin'),
    path('homeadmin/', main.homeadmin, name = 'homeadmin'),
    path('categoryadmin/', main.categoryadmin, name = 'categoryadmin'),
    path('comicadmin/', main.comicadmin, name = 'comicadmin'),
    path('user/', main.useradmin, name = 'useradmin'),
    path('chap/', main.chapadmin, name = 'chapadmin'),
  


]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)