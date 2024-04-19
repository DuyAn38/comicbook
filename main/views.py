from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import *



# user
def base(requert):
    return render(requert,'user/base.html')

def home(requert):
    return render(requert,'user/home.html')

def category(requert):
    return render(requert,'user/category.html')

def detai(requert):
    return render(requert,'user/detai.html')

def chap(requert):
    return render(requert,'user/chap.html')

def information(requert):
    return render(requert,'user/information.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Đăng nhập thành công.')
            return redirect('home')  
        else:
            # Đăng nhập thất bại, hiển thị form đăng nhập với thông báo lỗi
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
            return render(request, 'user/login.html')
    else:
        # Nếu không phải là phương thức POST, chỉ cần hiển thị form đăng nhập
        return render(request, 'user/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # checkpass
        if password != confirm_password:
            messages.error(request, 'Mật khẩu không khớp. Vui lòng nhập lại.')
            return render(request, 'user/register.html')
        
        # create
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Đăng ký thành công. Bây giờ bạn có thể đăng nhập.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {e}')
            return render(request, 'user/register.html')
    else:
        return render(request, 'user/register.html')


# admin
def baseadmin(requert):
    return render(requert,'admin/baseadmin.html')

def homeadmin(requert):
    return render(requert,'admin/homeadmin.html')

def categoryadmin(requert):
    return render(requert,'admin/categoryadmin.html')

def comic(requert):
    return render(requert,'admin/comic.html')

def user(requert):
    return render(requert,'admin/user.html')

def chap(requert):
    return render(requert,'admin/chap.html')

