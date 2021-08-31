from django.contrib import admin
from .models import BlogPost, Comment

class CommentInLine(admin.TabularInline):
    model = Comment

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)

