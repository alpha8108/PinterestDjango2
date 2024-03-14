from django.forms import ModelForm
from articleapp.models import Article
from projectapp.models import Project
from django import forms

class ArticleCreationForm(ModelForm):
    #게시글 쓸 때 위지윅 적용
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    
    #프로젝트다 불러오고 그와 동시에 고르지 않아도 되게끔.
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image','project', 'content'] # writer는 서버내에서 설정해줄거다? 