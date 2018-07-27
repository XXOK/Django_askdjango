from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm
import logging


def post_list(request):
    qs = Post.objects.all().prefetch_related('tag_set', 'comment_set')

    id_search = request.GET.get('id-search', '')
    if id_search:
        qs = qs.filter(id=id_search)

    title_search = request.GET.get('title-search', '')
    if title_search:
        qs = qs.filter(title__icontains=title_search)

    date_search = request.GET.get('date-search', '')
    if date_search:
        qs = qs.filter(updated_at__icontains=date_search)


    return render(request, 'blog/post_list.html',{
        'qs': qs,
        'id_search': id_search,
        'title_search': title_search,
        'date_search': date_search,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html',{
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.info(request, '포스팅 저장되었습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '수정이 완료되었습니다.')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_list(request):
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'blog/comment_list.html', {
        'comment_list': comment_list,
    })