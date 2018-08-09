# from django.http import HttpResponse
from django.shortcuts import render
import os

def hello(request):
    context = {}
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # context['hello'] = BASE_DIR
    context['hello'] = '!!!Hello World!!!'
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello world ! ")
