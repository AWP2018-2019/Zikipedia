from django import forms
from app import models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['text']