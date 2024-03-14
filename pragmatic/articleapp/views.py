from django.shortcuts import render

# reverse
from django.urls import reverse, reverse_lazy

#CRUD
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #장고에서 제공해주는 유저 생성 폼
from accountapp.forms import AccountUpdateForm
from django.views.generic.edit import FormMixin
from commentapp.forms import CommentCreationForm

#데코레이터 관련
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required
from articleapp.decorators import article_ownership_required

# 모델
from articleapp.models import Article

#폼
from articleapp.forms import ArticleCreationForm


# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    #아까 writer를 서버에서 지정해준다고 했잖음 / 프로필 앱의 뷰랑 비교하면서 코드 이해 ㄱㄱ
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk })
    

class ArticleDetailView(DetailView, FormMixin):
    model = Article 
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk })
    

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article' # 꼭 쓸 필요는 없다고함
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    success_url = reverse_lazy('articleapp:list')
    paginate_by = 10
