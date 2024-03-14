from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from .models import Project
from articleapp.models import Article
from subscribeapp.models import Subscription

from .forms import ProjectCreationForm
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.list import MultipleObjectMixin

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class=ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk })
    


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html' 

    paginate_by = 25

    #실질적으로 어떤 게시글을 가져올 지에 대한 필터링구문?
    # 접속해있는 유저가 이 게시판에 대한 구독정보가 있는지 없는지 홗인해주는게 필요 
    def get_context_data(self, **kwargs):
        project = self.object 
        user = self.request.user
        
        #유저가 로그인했는지
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                                 **kwargs)

    


class ProjectListView(ListView):
    model = Project 
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25
    

   


