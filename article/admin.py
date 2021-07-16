from django.contrib import admin
from .models import ArticlePost

# Register your models here.

# 注册ArticlePost到admin，便于管理
admin.site.register(ArticlePost)