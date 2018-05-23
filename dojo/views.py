from django.shortcuts import render,HttpResponse


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