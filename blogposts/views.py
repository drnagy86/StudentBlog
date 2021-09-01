from django.forms.models import modelform_factory
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import BlogPost, Comment
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



# # help from:
# # https://stackoverflow.com/questions/20785987/combining-detailview-and-createview-in-django-1-6

# #create the comment create view like normal
# class CommentView(CreateView):
#     model = Comment
#     fields = ('author', 'comment')

#     def get_success_url(self):
#         return reverse_lazy('blogpost_detail', kwargs={'pk' : self.get_object(BlogPost.objects.all().pk)})

# #combine the two views together
# class BlogPostCommentView(View):
#     def get(self, request, *args, **kwargs):
#         view = BlogPostDetialView.as_view()
#         return view(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         view = CommentView.as_view()
#         return view(request, *args, **kwargs)