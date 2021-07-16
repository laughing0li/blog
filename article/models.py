from django.db import models
# 导入第一次migrate命令生成的User模型
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# 博客文章数据模型
class ArticlePost(models.Model):

    # 文章的作者，多对一的关系，以User为外键，级联删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 文章标题为字符串字段
    title = models.CharField(max_length=100)

    # 文章的正文，保存大量的文本需要使用TextField
    body = models.TextField()

    # 用当前时间自动生成
    created = models.DateTimeField(default=timezone.now)

    # auto_now=True 表示该字段是自动添加的
    updated = models.DateTimeField(auto_now=True)

    # 用于在print的时候格式化输出
    def __str__(self):
        return self.title

    class Meta:

        # ordering接收一个元组，用于指定模型返回数据的排列顺序
        # ’-created‘表示数据应该以倒序排列，其中-表示降序
        # 如果没有-就表示升序排列
        ordering = ('-created',)