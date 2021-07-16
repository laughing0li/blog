"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # 参数'article/'指明了该App的访问路径
    # include 指明将路径发给下一步进行处理，就是发到article下的urls进行处理
    # namespace保证反查到唯一的url，即使是不同的App用了相同的url，但是因为
    # namespace不一样，所以也能工作
    # path('article/', include('article.urls', namespace='article')),
    path('article/', include('article.urls', namespace='article')),

]
