from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from main.models import *

def chapadmin(requert):
    chapter = Chap.objects.all()
    print(chapter)
    context = {
        'chapter': chapter
    }
    return render(requert,'admin/chapadmin.html', context)

def add_chap(request):
    if request.method == 'POST':
        form = ChapForm(request.POST, request.FILES)
        if form.is_valid():
            chap = form.save()  # Lưu chương mới vào cơ sở dữ liệu và nhận instance của chương
            images = request.FILES.getlist('listImages')
            for image in images:
                fs = FileSystemStorage()
                image_name = fs.save(image.name, image)
                image_chapter = ImagesChap(chap=chap, image=image_name)
                image_chapter.save()
            messages.success(request, 'Thêm chap thành công')
            return redirect('chapadmin')
        else:
            messages.error(request, 'Thêm chap thất bại')
    else:
        form = ChapForm()
    context = {
        'form': form,
    }
    return render(request, 'admin/addchapcomic.html', context)


def edit_chap(request, id):
    chap = get_object_or_404(Chap, pk=id)
    if request.method == 'POST':
        form = ChapForm(request.POST, request.FILES, instance=chap)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sửa truyện thành công')
            return redirect('chapadmin')
    else:
        form = ChapForm(instance=chap)
    return render(request, 'admin/updatechapcomic.html', {'form': form})


def delete_chap(request, id):
    chap = get_object_or_404(Chap, pk=id)
    if request.method == 'POST':
        chap.delete()
        messages.success(request, 'Xóa chap thành công')
        return redirect('chapadmin')

    return render(request, 'admin/chapadmin.html')
