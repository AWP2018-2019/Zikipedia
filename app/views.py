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
from models import Article, Category, User

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


class CategoryCreateView(LoginRequiredMixin, CreateView):
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
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'text', 'category']
    template_name = 'article_create.html'
    
    def form_valid(self, form):
        article = Article.objects.create(
            created_by=self.request.user,
            **form.cleaned_data
        )
        
        return redirect(reverse_lazy("article_detail", kwargs={"pk": article.id }))

class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'text', 'category']
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = Article.objects.get(pk=self.kwargs['pk'])
        article.title = form.cleaned_data['title']
        article.text = form.cleaned_data['text']
        article.category = form.cleaned_data['category']

        article.save()
        return redirect(reverse_lazy("article_detail", kwargs={"pk": self.kwargs['pk']}))
        
        
class CategoryEditView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_edit.html'

    def form_valid(self, form):
        category = Category.objects.get(pk=self.kwargs['pk'])
        category.name = form.cleaned_data['name']
        category.save()
        return redirect(reverse_lazy("category_detail", kwargs={"pk": self.kwargs['pk']}))
        
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    model = Article
    
    def get_success_url(self):
        return reverse_lazy('allarticles')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    template_name='category_delete.html'
    model=Category
    
    def get_success_url(self):
        return reverse_lazy('allcategories')


class RegisterView(CreateView):
    template_name= 'register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        # UserProfile.objects.create(user=user)
        return redirect('index')

class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect(reverse_lazy('index'))
        else:
            return render(request, "login.html", {"form": form})

@login_required    
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('index'))