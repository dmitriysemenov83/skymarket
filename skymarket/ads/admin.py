from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdsAdAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'price', 'author', 'created_at', 'description')


@admin.register(Comment)
class AdsCommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'created_at', 'ad')
