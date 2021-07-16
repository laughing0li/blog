from django.urls import path
from . import views

# 为该App添加一个实例命名空间，在反转url的时候，能够定位到指定的位置
# 即使有多个App都有相同的url也不会出现问题

app_name = 'article'

urlpatterns = [
    # list页面
    path('list/', views.article_list, name='article_list'),
    # detail页面
    path('detail/<int:id>/', views.article_detail, name='article_detail'),
    # 新建博客页面
    path('article-create/', views.article_create, name='article_create'),
    # 删除博客
    path('article-delete/<int:id>/', views.article_delete, name='article_delete')


]