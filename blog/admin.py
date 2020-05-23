from django.contrib import admin

from .models import Post
from .forms import PostAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('title', )}
    form = PostAdminForm
