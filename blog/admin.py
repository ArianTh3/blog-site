from django.contrib import admin
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'   
    list_display = ('title' , 'author','counted_views','status','published_date','created_date')
    list_filter = ('status', 'author')
    search_fields = ['title','content']
    


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'   
    list_display = ('name' , 'posts', 'approved', 'created_date')
    list_filter = ('posts', 'approved')
    search_fields = ['name', 'posts']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)