from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django import forms
from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().prefetch_related('tag_set', 'comment_set')
    paginate_by = 10

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url='/blog/')