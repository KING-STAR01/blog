from django.contrib import admin
from .models import Article, UserProfile, Comments

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on', 'active']
    list_editable = ['active']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'active', 'created_on']

admin.site.register(Article,ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(Comments)