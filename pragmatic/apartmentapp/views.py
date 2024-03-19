from django.shortcuts import render, HttpResponse

# Create your views here.

from .forms import MyForm

def my_form_view(request):
    form = MyForm()
    return render(request, 'apartmentapp/predict.html', {'form': form})
