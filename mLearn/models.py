from django.db import models
from django.contrib.auth.models import User
from django import forms
#from ckeditor_uploader.widgets import CKEditorUploadingWidget  # image 처리가능
from django.urls import reverse

# Create your models here.
class MLearn(models.Model):

    subject=models.CharField(max_length=30, verbose_name='제목')
    # subject = forms.CharField(
    #     max_length=200,
    #     widget=forms.TextInput(
    #         attrs={
    #             'style': 'border-color:blue',
    #             'placeholder': 'write tile here'
    #         }
    #     ))
    # category = models.CharField('카테고리', max_length=10, choices=TYPE_CHOICES)

    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    # writer=models.CharField(max_length=100, verbose_name='작성자', help_text='비회원경우, 별명 입력')

    content = models.TextField(verbose_name='내용')
    # content = models.TextField(verbose_name='내용', widget=CKEditorUploadingWidget())
    # content = RichTextUploadingField(verbose_name='내용')

    # upload = models.FileField(upload_to='uploaded/', verbose_name='업로드파일' )

    created_at = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 저장
    updated_at = models.DateTimeField(auto_now=True)  # 레코드 업데이트시 현재 시간으로 자동 저장

    class Meta:
        ordering = ['-id']   # - : reverse


