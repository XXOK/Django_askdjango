from django import forms
# from .models import Post


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('error')


class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField()