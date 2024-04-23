from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from main.models import *

def information(requert):
    categories = category.objects.filter(is_sub=False)
    context = {
        'categories': categories,
    }
    return render(requert, 'user/information.html', context)
    

def register(request):
    if request.method == 'POST':
        form = CreatememberForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('home')  
    else:
        form = CreatememberForm()
    return render(request, 'user/register.html', {'form': form})

def changepassword(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        return JsonResponse({'message': 'Mật khẩu đã được thay đổi thành công.'})
    else:
        return JsonResponse({'error': 'Phương thức không được hỗ trợ.'}, status=405)

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
