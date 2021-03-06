from django.contrib import admin

from .models import Comment, Follow, Group, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'author',
        'text',
    )
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'author'
    )
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'author',
    )
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
