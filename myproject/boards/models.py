"""
这里是我们定义Web应用程序数据实例的地方。models会由Django自动转换为数据库表
所有模型都是django.db.models.Model类的子类。每个类将被转换为数据库表
"""
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    """
    Adminer create the board
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    """
    Topic of each board
    """
    subject = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    """
    User release the post
    updated_by 字段设置 related_name='+' 。这指示Django我们不需要这
    种反向关系，所以它会被忽略（也就是说我们不需要关系用户修改过哪些帖子）
    """
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    create_by = models.ForeignKey(User, related_name='posts')
    update_by = models.ForeignKey(User, null=True, related_name='+')
