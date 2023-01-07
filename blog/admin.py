from django.contrib import admin
from .models import Article, UserProfile, Comments

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on']

admin.site.register(Article,ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(Comments)