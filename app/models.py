# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=20000)
    created_by = models.ForeignKey(User, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)
        

class Review(models.Model):
    text = models.CharField(max_length=25)
    article = models.ForeignKey(Article, related_name="reviews")
    created_by = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)