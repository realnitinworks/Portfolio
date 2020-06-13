from django.contrib import admin

from .models import Post, Comment
from .forms import PostAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('title', )}
    form = PostAdminForm


@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'post', 'body')
    readonly_fields = ('created', 'updated')
    
