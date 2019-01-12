# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    
    def __str__(self):
        return "Categoria {}".format(self.name)
        
    class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_by = models.ForeignKey(User, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(Category, related_name='articles')

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)
        


    
