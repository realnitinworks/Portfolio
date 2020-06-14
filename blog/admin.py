from django.contrib import admin

from .forms import PostAdminForm
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    readonly_fields = ("created", "updated")
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm


@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "active", "post", "body")
    readonly_fields = ("created", "updated")
