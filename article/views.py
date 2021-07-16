from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# 引入User模型
from django.contrib.auth.models import User

# 引入表单类
from .forms import ArticlePostForm
from .models import ArticlePost

# 引入Markdown语法
import markdown



def article_list(request):
    
    # 获取到数据库中所有的博客文章
    articles = ArticlePost.objects.all()

    # 需要传递给模板(templates) 的对象，这个对象是个字典
    context = { 'articles' : articles }

    # render函数，载入模板
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    # 根据id获取到相应的文章
    article = ArticlePost.objects.get(id=id)

    article.body = markdown.markdown(article.body, extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
    ])

    context = { 'article' : article }

    return render(request, 'article/detail.html', context)

# 添加博客的视图
def article_create(request):
    # 首先判断是否是提交动作
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data = request.POST)
        # 判断提交的数据是否满足ArticlePostForm的要求
        if article_post_form.is_valid():
            # 保存数据，但是commit=false，所以暂时不提交到数据库
            new_article = article_post_form.save(commit=False)
            # 指定数据库中，id=1的用户为作者
            new_article.author = User.objects.get(id=1)
            # 将新博客保存到数据库
            new_article.save()
            # 返回到博客列表
            return redirect("article:article_list")
        else:
            # 如果数据不合格，那么久返回错误
            return HttpResponse("Please Try it again")
    else:
        # 如果不是POST提交数据的动作，那么就是获取新表单的东西
        # 就渲染一个表单进行数据的填写
        article_post_form = ArticlePostForm()
        context = { 'article_post_form' : article_post_form }
        return render(request, 'article/create.html', context)

# 理由csrf的方式安全删除对应的博客
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse('Only Allow POST request')
    

# 
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    # 先判断，进来这个视图的请求是否是POST
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data = request.POST)
        # 将数据更新，然后存储
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 返回到对应id的博客详情
            return redirect('article:article_detail', id=id)
        else:
            return HttpResponse('Invalid Input, Please try again')
    else:
        # 将需要修改的博客渲染到页面
        article_post_form = ArticlePostForm()
        context = { 'article':article, 'article_post_form': article_post_form }
        return render(request, 'article/update.html', context)


    
