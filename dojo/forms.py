from django import forms
from .models import Post
from django.shortcuts import redirect


# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_length_3_validator])
#     content = forms.CharField(widget=forms.Textarea)

    # def save(self, commit=True):
    #     post = Post(**self.cleaned_data)
    #     if commit:
    #         post.save()
    #         return post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']