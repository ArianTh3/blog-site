from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 1

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'   
    list_display = ('title' , 'author','counted_views','status','published_date','created_date')
    list_filter = ('status', 'author')
    search_fields = ['title','content']
    inlines = [ContentBlockInline]
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'   
    list_display = ('name' , 'posts', 'approved', 'created_date')
    list_filter = ('posts', 'approved')
    search_fields = ['name', 'posts']




 
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
