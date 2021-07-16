from django import forms
from django.contrib.auth.models import User

# 创建用户的登录表单
# forms.Form需要手动配置每个字段，
# 它适用于不与数据库进行直接交互的功能。
# 用户登录不需要对数据库进行任何改动，因此直接继承forms.Form就可以了。
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# 创建用户的注册表单
# 表单类继承了forms.ModelForm，
# 这个父类适合于需要直接与数据库交互的功能，
# 比如新建、更新数据库的字段等。如果表单将用于直接添加或编辑Django模型，
# 则可以使用 ModelForm来避免重复书写字段描述
class UserRegisterForm(forms.ModelForm):
    
    # 通常注册用户都需要输入两次密码，进行验证
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        #  指明数据模型的来源，这里数据的来源是User
        model = User
        
        # 定义表单需要填入的字段
        fields = ('username', 'email')
    
    # def clean_[字段]这种写法Django会自动调用，来对单个字段的数据进行验证清洗。
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError('Check your password, make sure there are the same')
