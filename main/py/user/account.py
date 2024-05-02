from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from main.models import *


def information(requert):
    users = User.objects.all()
    print(users)
    context = {
        'users': users
    }
    return render(requert,'user/information.html', context)

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đăng ký thành công')
            return redirect('login')
        else:
            messages.error(request, 'Đăng ký thất bại')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)



def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Mật khẩu của bạn đã được thay đổi thành công!')
            return redirect('changepassword')
        else:
            messages.error(request, 'Đổi mật khẩu không thành công!.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/changepassword.html', {'form': form})



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
