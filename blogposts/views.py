from django.forms.models import modelform_factory
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import BlogPost
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogposts/blogpost_list.html'

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
    model = BlogPost
    template_name = 'blogposts/blogpost_new.html'
    fields = ('title', 'body', )

    def form_valid(self, form: modelform_factory) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


