from django.forms import ModelForm
from .models import Article, Comments, UserProfile
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'image', 'category']

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'cols':65, 'class':'form-control'}),
            'title': forms.TextInput(attrs={'length':50,'class':'form-control'})
        }

class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['image', 'bio']

    