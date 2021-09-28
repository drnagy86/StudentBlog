from django import forms
from django import forms
from django.forms import ModelForm, Form, widgets
from django.views.generic.detail import DetailView

from .models import Comment, BlogPost, Tag

class CommentCreateForm(ModelForm):    
    
    class Meta(ModelForm):
        model = Comment
        fields = ('author', 'comment', )
        


class BlogPostCreateForm(ModelForm):

    # add a new field not on the model
    # new_tag = forms.CharField(max_length=25)

    class Meta(ModelForm):
        model = BlogPost
        
        fields = ('title', 'body','tags', )

    title = forms.CharField()
    body = forms.TextInput()

    tags = forms.ModelMultipleChoiceField(
        queryset= Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple

    )

    def clean(self):
        super(BlogPostCreateForm, self).clean()


        return self.cleaned_data

    
       
        







    



