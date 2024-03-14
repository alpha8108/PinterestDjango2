from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from projectapp.models import Project

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article') # 유저객체에서 article에 접근할 떄 쓰는 이름이라 writer이지만 article이라고 명한것.
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='article')

    title = models.CharField(max_length=200, null=True) # 제목을 꼭 적어야한다는 고정관념 탈피? ㅋ
    image = models.ImageField(upload_to='article/', null=False) #편의상 이미지는 항상 넣도록
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)













