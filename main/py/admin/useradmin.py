from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *

def useradmin(requert):
    users = User.objects.all()
    print(users)
    context = {
        'users': users
    }
    return render(requert,'admin/useradmin.html', context)


def add_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm người dùng thành công')
            return redirect('useradmin')
        else:
            messages.error(request, 'Thêm truyện thất bại')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'admin/adduser.html', context)


def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa người dùng thành công')
            return redirect('useradmin')
    else:
        form = UserForm(instance=user)
        messages.success(request, 'Sửa người dùng that bai')
    return render(request, 'admin/updateuser.html', {'form': form})




def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Xóa người dùng thành công')
        return redirect('useradmin')

    return render(request, 'admin/useradmin.html')