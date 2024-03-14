from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# reverse
from django.urls import reverse, reverse_lazy

#CRUD
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #장고에서 제공해주는 유저 생성 폼
from accountapp.forms import AccountUpdateForm
from django.views.generic.list import MultipleObjectMixin

#데코레이터 관련
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required

from articleapp.models import Article


has_ownership = [account_ownership_required, login_required]

# Create your views here.

class AccountCreateView(CreateView): #CBV만들떄 주요한 파라미터 만든다고했는데        
    model= User
    form_class = UserCreationForm # 계정은 중요한거라서 장고에서 폼을 제공해줌(만들필요 X )
    success_url = reverse_lazy('accountapp:hello_world')  #성공했으면 가는 / 그리고 reverse_lazy는 클래스형에서 씀 
    template_name = 'accountapp/create.html'  #회원가입을 할 때 보일 비주얼폼 

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # 다른 사람이 와도 내 정보를 보게, 
    template_name = 'accountapp/detail.html'

    paginate_by = 10

    #ㅈㄴ 이해안되는 코드 ;;
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)
    
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model= User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') 
    template_name = 'accountapp/update.html'  

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

