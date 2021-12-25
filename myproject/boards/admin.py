"""
这个文件为一个django内置的应用程序Django Admin的配置文件
"""
from django.contrib import admin
from .models import Board

admin.site.register(Board)



















