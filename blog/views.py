from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.all()

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
            return redirect(post)
            # post.get_absolute_url() -> post 안에 get_absolute_url() 구현되어 있음
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
            return redirect(post)
            # post.get_absolute_url() -> post 안에 get_absolute_url() 구현되어 있음
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })