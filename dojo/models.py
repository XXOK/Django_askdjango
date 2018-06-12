from django.db import models
from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('error')


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[min_length_3_validator]
    )
    content = models.TextField(

    )
    ip = models.CharField(
        max_length=20
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )