# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from forms import CategoryForm
from models import Article, Category

# def index(request):
#     return HttpResponse("Welcome to Zikipedia!")

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
    
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    form = CategoryForm()
    return render(request, "article_detail.html", 
    {"article": article, "form": form})