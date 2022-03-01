from django.contrib import admin
from django.contrib import admin
from .models import Category, Post, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category view in Admin Page"""
    list_display = ('name', 'desc_box')
    search_fields = ('name', 'desc_box')

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Post view in Admin Page"""
    list_display = ('title', 'slug', 'created', 'author')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('author__username', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)