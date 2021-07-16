from django import forms

from .models import ArticlePost

# 用于书写文章的表单类，使用forms.ModerForm或者forms.Form一样
# 因为他们都是继承自BaseForm类
class ArticlePostForm(forms.ModelForm):

    class Meta:
        #  指明数据模型的来源，这里数据的来源是ArticlePost
        model = ArticlePost

        # 定义表单需要填入的字段
        # 因为关于创建和修改的时间是自动生成的，author一直是管理员，都不需要填入
        # 只有title和内容需要填入
        fields = ('title', 'body')