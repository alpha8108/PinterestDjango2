from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    #게시글 쓸 떄 프로젝트 고르는데 그 떄 프로젝트 이름으로 나오도록
    def __str__(self):
        return f'{self.pk}:{self.title}'
