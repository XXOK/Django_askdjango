from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from .forms import PostForm
from .models import Post
import os


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form': form,
    })


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    # 값이 비었을때 0으로 처리해라
    return HttpResponse(result)


def profile(request, name, age):
    a = name
    b = age
    return render(request, 'dojo/profile.html',{
        'name': a,
        'age': b,
    })


def post_list1(request):
    # HttpResponse 를 통한 응답
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>반갑습니다, 여러분들 :)</p>
    '''.format(name=name))


def post_list2(request):
    # template 을 통한 응답
    name = '공유'
    return render(request, 'dojo/post_list2.html',{
        'name': name
    })


def post_list3(request):
    # Json 형태를 통한 응답
    return JsonResponse({
        'message': '안녕 파이썬&장고 이건 Jason 이야',
        'items': ['Python','Django','Celery','Azure','AWS'],
    }, json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    # 특정 파일 다운로드 응답
    filepath = '/Users/yeonsin/Django_askdjango/bug.xlsx'
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='Django_askdjango/bug.xlsx')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


