from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django import forms
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


post_new = PostCreateView.as_view()

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url='/blog/')