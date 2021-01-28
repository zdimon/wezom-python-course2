from django.shortcuts import render
from game.models import Page, Images
from django.http import HttpResponse
from game.forms import GameuserForm


from game.models import Gameuser

def find_user(login,password):
    user = None
    try:
        user = Gameuser.objects.get(login=login)
        if user.password == password:
            return user
    except Exception as e:
        print(e)
    return user



def index(request):
    user = None
    if request.method == 'POST':
        form = GameuserForm(request.POST, request.FILES)
        login = request.POST['login']
        password = request.POST['password']
        user = find_user(login,password)
        if not user:
            if form.is_valid():
                user = form.save()
    else:
        form = GameuserForm()

    return render(request, 'index.html', {'form': form, 'user': user})

def game(request):
    return render(request, 'game.html')
