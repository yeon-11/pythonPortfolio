# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # 불러와서 사용


def main(request):  # 메인
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# numpy(np)
import numpy as np
from django.shortcuts import render


def syntax(request):
    template = loader.get_template('syntax.html')
    context = {
        'firstname': '지연',
        'lastname': '박',
    }
    return HttpResponse(template.render(context, request))


def ifelse(request):
    template = loader.get_template('ifelse.html')
    context = {
        'greeting': 1,
    }
    return HttpResponse(template.render(context, request))


def forloop(request):
    template = loader.get_template('forloop.html')
    context = {
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }]
    }
    return HttpResponse(template.render(context, request))


def members(request):
    arr = np.array([1, 2, 3, 4, 5])  # 배열 생성
    total = np.sum(arr)  # 배열 합
    mean = np.mean(arr)  # 배열 평균

    context = {
        'greeting': 1,
        'total': total,
        'mean': mean,
    }
    return render(request, 'members.html', context)

# Create your views here.
