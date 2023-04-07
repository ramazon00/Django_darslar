from django.shortcuts import render
from articles.models import Article
from django.views.generic import ListView, DetailView

class home(ListView):
    model  = Article
    template_name = 'home.html'