from django import forms
from .models import Post, Category


#choices = [('coding', 'coding'), ('athletics', 'athletics'), ('entertainment', 'entertainment'),]
choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your title here!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag your title here!'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tell us your name here!'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Say anything here!'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your title here!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag your title here!'}),
             #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tell us your name here!'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Say anything here!'}),

        }