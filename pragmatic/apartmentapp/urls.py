from django.urls import path
from .views import *

app_name='apartmentapp'

urlpatterns = [
    path('predict/', my_form_view,  name='predict' )

]