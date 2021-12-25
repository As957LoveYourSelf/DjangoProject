"""
这是我们处理Web应用程序请求(request)/响应(response)周期的文件
"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


def home(request):
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})









