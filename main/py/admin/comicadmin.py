
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from main.models import comic
from main.models import *



def comicadmin(request):
    comics = comic.objects.all()
    context = {
        'comics': comics, 
    }
    return render(request, 'admin/comicadmin.html', context)


def add_comic(request):
    form = ComicForm()
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm truyện thành công')
            return redirect('comicadmin')
        else:
            messages.error(request, 'Thêm truyện thất bại')
    else:
        form = ComicForm()
    context = {
        'form': form,
    }
    return render(request, 'admin/addcomic.html', context)


def edit_comic(request, id):
    comic_one = get_object_or_404(comic, pk=id)
    if request.method == 'POST':
        form = ComicForm(request.POST,request.FILES, instance=comic_one)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa truyện thành công')
            return redirect('comicadmin')
    else:
        form = ComicForm(instance=comic_one)
    return render(request, 'admin/updatecomic.html', {'form': form})


def delete_comic(request, id):
    cmic = get_object_or_404(comic, pk=id)
    if request.method == 'POST':
        cmic.delete()
        messages.success(request, 'Xóa truyện thành công')
        return redirect('comicadmin')

    return render(request, 'admin/comicadmin.html')
