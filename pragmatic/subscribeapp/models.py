from django.db import models

from django.contrib.auth.models import User
from projectapp.models import Project
# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    #메타정보로 보내준다?? 
    class Meta:
        unique_together = ('user', 'project')
