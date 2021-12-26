from django import forms
from django.contrib.auth.models import User        # 'auth.User' table
from django.contrib.auth.forms import UserCreationForm
# from .models import JoinMember


# ModelForm활용한 로그인 접근
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password',]

# Form을 이용하여
# class JoinForm(forms.Form):
    # username = forms.CharField()
    # last_name = forms.CharField()
    # first_name = forms.CharField()
    # password = forms.CharField()
    # email = forms.CharField()
    # address = forms.CharField()

    # class Meta:
    #     model = JoinMember
    #     fields = ('username', 'address', 'first_name', 'last_name', 'email', 'password',)


# ModelForm을 이용하여
class JoinForm(forms.ModelForm):

    class Meta:
        # model = JoinMember
        model = User
        fields = ['username', 'email', 'password', ]
        # fields = '__all__'

# class JoinUserForm(forms.ModelForm):
class JoinUserForm(UserCreationForm):
    address = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ('username', 'address', 'email', 'password1', 'password2',)

#UserCreationForm을 통한 간편 회원 가입
# class JoinForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email',)


