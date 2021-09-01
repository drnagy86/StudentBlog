from django.contrib import admin
from .models import BlogPost, Comment

class CommentInLine(admin.TabularInline):
    model = Comment

# lots of help from:
# https://stackoverflow.com/questions/60497516/django-add-comment-section-on-posts-feed

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blogpost', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', )
    search_fields = ('name', 'comment',)

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)

