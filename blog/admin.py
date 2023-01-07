from django.contrib import admin
from .models import Article, UserProfile, Comments

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on']

<<<<<<< HEAD
admin.site.register(Article,ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(Comments)
=======
class CommentAdmin(admin.ModelAdmin):
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active = True)


admin.site.register(Article,ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(Comments, CommentAdmin)
>>>>>>> 830b7db (blog website)
