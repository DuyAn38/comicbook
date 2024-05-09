from django.contrib import admin
from .models import *

admin.site.register(category)
admin.site.register(comic)
admin.site.register(Chap)
admin.site.register(ImagesChap)
admin.site.register(member)
admin.site.register(Comment)
admin.site.register(Follow)