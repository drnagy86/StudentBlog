from django.http.request import HttpRequest
from django.urls.base import reverse
from django.views.generic.detail import SingleObjectMixin
from blogposts.forms import BlogPostCreateForm, CommentCreateForm
from django import forms
from django.forms.models import modelform_factory
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from .models import BlogPost, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogposts/blogpost_list.html'

class BlogPostShortListView(ListView):
    model = BlogPost
    template_name = 'blogposts/blogpost_short_list.html'


class BlogPostDetialView(DetailView):
    model = BlogPost
    template_name = 'blogposts/blogpost_detail.html'

    

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ('title','body',)
    template_name = 'blogposts/blogpost_edit.html'
    success_url = reverse_lazy('blogpost_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blogposts/blogpost_delete.html'
    success_url = reverse_lazy('blogpost_list')

    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    # model = BlogPost
    # template_name = 'blogposts/blogpost_new.html'
    # fields = ('title', 'body','tags' )

    form_class = BlogPostCreateForm
    model = BlogPost
    template_name = 'blogposts/blogpost_new.html'
    
    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk':self.object.pk})
    

    def form_valid(self, form: modelform_factory) -> HttpResponse:
        form.instance.author = self.request.user


        return super().form_valid(form)



class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blogposts/blogpost_comments_new.html'
    fields = ('blogpost','author', 'comment')
    
    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk':self.object.pk})
        














class BlogPostCommentDetialView(DetailView):
    model = BlogPost
    template_name = 'blogposts/blogpostcomment_detail.html'

    # set up the detail view for blogposts to return the comment create form with its context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm()

        return context
        
    
#combine the two views together
class BlogPostCommentView(View):
    def get(self, request, *args, **kwargs):
        view = BlogPostCommentDetialView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        # view = CommentFormCreateView.as_view()
        return view(request, *args, **kwargs)

class CommentFormView(SingleObjectMixin, FormView):
    template_name = 'blogposts/blogpost_detail.html'
    form_class = CommentCreateForm
    model = BlogPost

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        return super(CommentFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk':self.object.pk})
        
        

    def form_valid(self, form):
        self.object = self.get_object()

        self.object.save()
        


        return super(CommentFormView, self).form_valid(form)

    
    


