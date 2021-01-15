from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'name': 'Dima'})

def login(request):
    return render(request, 'login.html')