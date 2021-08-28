from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import BlogPost
from django.urls import reverse_lazy


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogposts/blogpost_list.html'

class BlogPostDetialView(DetailView):
    model = BlogPost
    template_name = 'blogposts/blogpost_detail.html'

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title','body',)
    template_name = 'blogposts/blogpost_edit.html'
    success_url = reverse_lazy('blogpost_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogposts/blogpost_delete.html'
    success_url = reverse_lazy('blogpost_list')

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogposts/blogpost_new.html'
    fields = ('title', 'body', 'author',)


