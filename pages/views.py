from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from blogposts.models import BlogPost

class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

