#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #불러온다는건 그걸 사용하겠다는 의미
from .models import Member #모델 불러오기
#메인
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
#numpy
import numpy as np
from django.shortcuts import render

def syntax(request):
    template = loader.get_template('syntax.html')
    context = {
        'firstname':'영일',
        'lastname':'황',
    }
    return HttpResponse(template.render(context, request))

def ifelse(request):
    template = loader.get_template('ifelse.html')
    context = {
        'greeting':2,
    }
    return HttpResponse(template.render(context, request))

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
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

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))