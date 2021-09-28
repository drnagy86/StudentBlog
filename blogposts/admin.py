from django.contrib import admin
from .models import BlogPost, Comment, Tag

class CommentInLine(admin.TabularInline):
    model = Comment

class TagInLine(admin.TabularInline):
    model = Tag

# lots of help from:
# https://stackoverflow.com/questions/60497516/django-add-comment-section-on-posts-feed

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blogpost', 'created_on', 'approved', 'tags')
    list_filter = ('approved', 'created_on', )
    search_fields = ('name', 'comment', 'tags')

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
        # TagInLine,

    ]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)

