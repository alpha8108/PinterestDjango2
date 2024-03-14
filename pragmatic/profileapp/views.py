from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy

#CRUD
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #장고에서 제공해주는 유저 생성 폼
from accountapp.forms import AccountUpdateForm

#데코레이터 관련
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required
from profileapp.decorators import profile_ownership_required

#모델
from profileapp.models import Profile

#폼
from profileapp.forms import ProfileCreationForm


has_ownership = [account_ownership_required, login_required]


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name='target_profile'
    form_class=ProfileCreationForm
    template_name = 'profileapp/create.html'

    #이건 아마..로그인한 다른 사람이 profile을 만들지 못하게 본인이 본인 프로필만 만들 수 있게하는그런?
    def form_valid(self, form): #프로필만들떄 폼에 넣었던 데이터가 저self, form에 있는 form에 있다. 
        temp_profile = form.save(commit=False) #임시로 저장하는것. 저장한 이미지,닉네임,메시지 3가지 데이터는있는데 유저라는 데이터는 없는것 
        temp_profile.user = self.request.user # 저 변수에 요청을(프로필 만들겠다는)보낸 당사자 유저로 정해줄거임 
        temp_profile.save() #그리고나서 최종적으로 저장.
        return super().form_valid(form) # CreateView의 원래 결과를 리턴해줄거임
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})#여기서 self에서 가지고 있는 object는 Profile임
    


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name='target_profile'
    form_class=ProfileCreationForm
    template_name = 'profileapp/update.html'

    # 수정이 끝나면 유저pk를 받아야하는 디테일페이지로 돌아가게 한 코드 
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
