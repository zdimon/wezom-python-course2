from django.shortcuts import render
from game.models import Page, Images
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'name': 'Dima'})

def login(request):
    return render(request, 'login.html')

def contact(request):
    
    if request.method == 'POST':
        message = 'Thank you!'
    else:
        message = 'Hello please write your message'
    print(request.POST.get('message','default value'))
    return render(request, 'contact.html', {'message': message})

def page(request,name):
    print(name)
    #pages = Page.objects.filter(fieldname='value',)
    try:
        page = Page.objects.get(alias=name)
    except Exception as e:
        print(e)
        page = Page.objects.get(alias='main')
    return render(request, 'page.html', {"page": page})