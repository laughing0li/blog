from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm


def user_login(request):
    if request.method == 'POST':
        # 从request.POST 里面获取到返回的数据，然后创建一个表单实例
        user_login_form = UserLoginForm(data=request.POST)
        
        # 每个表单实例都内置了is_valid方法
        # 它会根据该模型定义，来判断输入的内容是否符合规则
        # 然后返回布尔值
        if user_login_form.is_valid():
            # 而且所有的表单数据都会转存到一个叫cleaned_data的属性
            # 该属性为字典类型的数据
            data = user_login_form.cleaned_data
            # 验证输入的用户信息
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 如果用户存在，则使用login将用户的信息保存到session中
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse('Incorrect password or username, please try again')
        else:
            return HttpResponse('Incorrect format of password or username, try again')
            
            # 获取到登录的页面
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse('Please use Get or Post request')

def user_logout(request):
    logout(request)
    return redirect('article:article_list')

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():

            new_user = user_register_form.save(commit=False)
            # 为新用户添加密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存数据，并且将新用户登录
            login(request, new_user)
            return redirect('article:article_list')
        else:
            return HttpResponse('Invalid Form, please try again')
    elif request.method == 'GET':
        user_register_form = UserLoginForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse('Please use Get or Post request')
