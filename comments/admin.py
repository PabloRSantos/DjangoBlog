from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'post', 'date', 'publish']
    list_display_links = ['id', 'name', 'email']
    list_editable = ['publish']


admin.site.register(Comments, CommentsAdmin)
