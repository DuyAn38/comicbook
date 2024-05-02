from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *

def categoryadmin(request):
    categories = category.objects.filter(is_sub=False)
    context = {
        'categories': categories,  
    }
    return render(request, 'admin/categoryadmin.html', context)
    

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm thể loại thành công')
            return redirect('categoryadmin')
        else:
            messages.error(request, 'Thêm thể loại thất bại')
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'admin/addcategory.html', context)


def edit_category(request, id):
    cate = get_object_or_404(category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=cate)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa thể loại thành công')
            return redirect('categoryadmin')
    else:
        form = CategoryForm(instance=cate)
    return render(request, 'admin/updatecategory.html', {'form': form})


def delete_category(request, id):
    cate = get_object_or_404(category, pk=id)
    if request.method == 'POST':
        cate.delete()
        messages.success(request, 'Xóa thể loại thành công')
        return redirect('categoryadmin')
    return render(request, 'admin/categoryadmin.html')
