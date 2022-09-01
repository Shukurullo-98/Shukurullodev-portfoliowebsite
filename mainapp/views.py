from django.shortcuts import render

from .models import Blog, Portfolio, AboutPage
from django.views import generic


class HomePage(generic.TemplateView):
    template_name = 'index.html'


class AboutView(generic.ListView):
    template_name = 'about.html'
    context_object_name = 'abouts'
    queryset = AboutPage.objects.all()


class PostView(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'
    queryset = Blog.objects.all()


class PostDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog-single.html'
    context_object_name = 'blogs'


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolio'
    queryset = Portfolio.objects.all()


