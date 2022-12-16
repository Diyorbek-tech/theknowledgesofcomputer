from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Blogmodel

# Create your views here.

class HomeClass(TemplateView):
    template_name = 'index.html'

class BlogClass(ListView):
    model = Blogmodel
    template_name = 'blog.html'
    context_object_name = "blogslist"