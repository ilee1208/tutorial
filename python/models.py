from django.db import models
from django.urls import reverse

# Create your models here.
class Python(models.Model):

    subject=models.CharField(max_length=30, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)  # 레코드 생성시 현재 시간으로 자동 저장
    updated_at = models.DateTimeField(auto_now=True)  # 레코드 업데이트시 현재 시간으로 자동 저장

    class Meta:
        ordering = ['-id']   # - : reverse



