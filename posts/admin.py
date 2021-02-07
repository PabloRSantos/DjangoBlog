from posts.models import Post
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'author', 'date', 'category', 'publish']
    list_display_links = ['id', 'title']
    list_editable = ['publish']
    summernote_fields = ['content']


admin.site.register(Post, PostAdmin)
