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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment view in Admin Page"""
    list_display = ('post', 'created', 'author')
    search_fields = ('body', 'author__username')
    list_filter = ('author__username', 'created')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact view in Admin Page"""
    list_display = ('first_name', 'last_name', 'email', 'created')
    search_fields = ('first_name', 'last_name', 'email', 'body')
    list_filter = ('first_name', 'last_name', 'email')
