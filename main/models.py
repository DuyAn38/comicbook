import requests
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from rest_framework import serializers
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

#the loai
class category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_genre', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
#truyen
class comic(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True,blank=True)
    category = models.ManyToManyField(category, related_name='story_category', blank=True)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True)                               
    status = models.BooleanField(default=False, null=True, blank=False)
    Describe = models.TextField(null=True)
    view = models.IntegerField(default=0)
    count_comment = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    story_new = models.BooleanField(default=False, null=True, blank=False)
    def __str__(self):
        return self.name
    
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
#chap
class Chap(models.Model):
    story = models.ForeignKey(comic, on_delete=models.CASCADE, related_name='chapters')
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    date = models.DateField(default=timezone.now, null=True)
    view = models.IntegerField(default=0)
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    def __str__(self):
        return self.story.name + ' - ' + str(self.name)
#hinh anh cua chap
class ImagesChap(models.Model):
    chap = models.ForeignKey(Chap, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.chap.story.name

#thanh vien
class member(models.Model):
    name = models.CharField(max_length =200,null=True)
    user_name = models.CharField(max_length =200,null=True)
    email = models.EmailField(max_length =200,null=True)
    password = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    profile_image = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
    
#form tao tai khoan
class CreatememberForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

#sua thong tin thanh vien
class CustommemberChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')

class Comment(models.Model):
    user = models.ForeignKey(member, on_delete=models.SET_NULL, null=True, blank=True)
    story = models.ForeignKey(comic, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(null=True, blank=False)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return self.story