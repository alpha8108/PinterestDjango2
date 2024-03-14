from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic import RedirectView, ListView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from articleapp.models import Article
from projectapp.models import Project 
from subscribeapp.models import Subscription

# Create your views here.

method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    
    def get(self, request, *args, **kwargs):

        #project_pk 를가지고 있는 project를 찾는데 없다면 404뜨게하라 ? 
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user 

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)
    
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article # 근데 나중에 쿼리셋을 바꿀꺼라 의미는 없긴하다고함? 
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    #쿼리셋 관련함수 가지고오는 게시글들의 조건을 바꿀 수 있음
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list