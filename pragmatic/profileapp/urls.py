
from django.urls import path
from .views import*

app_name='profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]