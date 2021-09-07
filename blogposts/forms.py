from django import forms
from django import forms
from django.forms import ModelForm, Form, widgets
from django.views.generic.detail import DetailView

from .models import Comment, BlogPost

class CommentCreateForm(ModelForm):    
    
    class Meta(ModelForm):
        model = Comment
        fields = ('author', 'comment', )
        


class BlogPostCreateForm(ModelForm):
    class Meta(ModelForm):
        model = BlogPost
        fields = ('title', 'body','tags' )

        


    



