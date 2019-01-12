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
    categories = Category.objects.all()
    articles = Article.objects.order_by('-created_at')[0:6]
    return render(request, "index.html", {"categories": categories, "articles": articles})

    
def all_articles(request):
    article_list=Article.objects.all()
    return render(request,'allarticles.html',{'article_list': article_list}) #de vazut cum facem ruta
    

def all_categories(request):
    category_list=Category.objects.all()
    return render(request,'allcategories.html',{'category_list': category_list}) #de vazut cum facem ruta
    
def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "article_detail.html", 
        {"article": article})   
    
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_create.html'
    def form_valid(self, form):
        category=Category.objects.create(
            **form.cleaned_data
            )
            
        return redirect(reverse_lazy("category_detail", kwargs={"pk": category.id}))        

    # {"article": article, "form": form})
    
def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "category_detail.html", {"category": category})
    
class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'text', 'category']
    template_name = 'article_create.html'
    
    def form_valid(self, form):
        article = Article.objects.create(
            created_by=self.request.user,
            **form.cleaned_data
        )
        
        return redirect(reverse_lazy("article_detail", kwargs={"pk": article.id }))

