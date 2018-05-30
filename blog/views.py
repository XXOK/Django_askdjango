from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


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
    post =  get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html',{
        'post': post,
    })