from django.contrib import admin
from django.db import models
from .models import Subscription,Ott_type,Genre,Content,Usersubscription,Comment

class ContentAdmin(admin.ModelAdmin):
    list_display = ("title","ott_type","genre","subscription")
    prepopulated_fields = {"slug":("title",)}

class UsersubscriptionAdmin(admin.ModelAdmin):
    list_display = ("username","subscription","date")
class CommentAdmin(admin.ModelAdmin):
    list_display = ("username","ratings")

admin.site.register(Ott_type)
admin.site.register(Subscription)
admin.site.register(Genre)
admin.site.register(Content,ContentAdmin)
admin.site.register(Usersubscription,UsersubscriptionAdmin)
admin.site.register(Comment,CommentAdmin)