from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 제일먼저 프로필모델과 유저객체를 하나씩 연결해준다는 것 
    
    image= models.ImageField(upload_to='profile/', null=True) # media 밑에 profile이라는 경로가 추가되고 그 안에 들어간다는 것 
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)