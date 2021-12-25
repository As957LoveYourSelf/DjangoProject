"""
这个文件用来写当前应用程序的单元测试
"""
from django.test import TestCase
from django.core.urlresolvers import reverse
from .views import home
from django.urls import resolve


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)



