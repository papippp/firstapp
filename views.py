from django.shortcuts import render
from django.http import HttpResponse

from . import forms

# Create your views here.
def homepage(request):
    return HttpResponse('A journey of a thousand miles start with one step.')

def index(request):
    form = forms.ApplicationForm()
    if request.method == 'POST':
        form = forms.ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'home.html', context)
def overview(request, name):
    context = {'name':name}
    return render(request, 'home.html', context)