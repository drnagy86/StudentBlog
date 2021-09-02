from django import forms
from django import forms
from django.forms import ModelForm, Form, widgets
from django.views.generic.detail import DetailView

from .models import Comment, BlogPost

class CommentCreateForm(ModelForm):    
    
    class Meta(ModelForm):
        model = Comment
        fields = ('author', 'comment',)


    



