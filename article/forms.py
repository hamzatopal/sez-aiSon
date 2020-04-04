from django import forms
from .models import Article
from django.forms import ModelForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content','article_image']

    