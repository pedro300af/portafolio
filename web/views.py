from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'web/index.html')
# Create your views here.
