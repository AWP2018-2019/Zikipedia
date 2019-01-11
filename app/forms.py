from django import forms
from app import models

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']