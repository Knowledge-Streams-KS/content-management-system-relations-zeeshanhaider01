from django import forms
from .models import Category, User

class CreateCategoryForm(forms.Form):
    name=forms.CharField(max_length=100)

class CreateUserForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

class CreateArticleForm(forms.Form):
    title=forms.CharField(max_length=100)
    Content=forms.CharField(max_length=5000)
    Category=forms.ModelMultipleChoiceField(Category.objects.all(),widget=forms.CheckboxSelectMultiple)
    author=forms.ModelMultipleChoiceField(User.objects.all(),widget=forms.CheckboxSelectMultiple)