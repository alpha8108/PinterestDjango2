from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.

#CRUD
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #장고에서 제공해주는 유저 생성 폼
from accountapp.forms import AccountUpdateForm

#데코레이터 관련
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import comment_ownership_required

from .models import Comment
from .forms import CommentCreationForm
from articleapp.models import Article

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    #아 이 코드가 이해가 더럽게 안된단 말이지....
    def form_valid(self, form):       
        temp_comment = form.save(commit=False)       
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])       
        temp_comment.writer = self.request.user          
        temp_comment.save()     
        return super().form_valid(form)       

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk }) #object는 코멘트고 코멘트를 단 article의 pk로 간다는것. 

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'commentapp/delete.html'
    context_object_name = 'target_comment'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk }) #object는 코멘트고 코멘트를 단 article의 pk로 간다는것. 



