from django.shortcuts import render
from game.models import Page, Images
from django.http import HttpResponse
from game.forms import GameuserForm
from game.models import Gameuser, Card
from game.utils import dial_cards_to_user, put_card_on_table_json, update_online_users_in_json
import json

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
    for u in Gameuser.objects.filter(is_online=True):
        dial_cards_to_user(u)
    return render(request, 'game.html')


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def put_card_on_table(request):
    data = json.loads(request.body)
    user = Gameuser.objects.get(login=data['login'])
    card = Card.objects.get(pk=data['card_id'])
    put_card_on_table_json(user,card)
    return HttpResponse('OK')

@csrf_exempt
def start_game(request):
    data = json.loads(request.body)
    user = Gameuser.objects.get(login=data['login'])
    user.state = 'gessor'
    user.save()
    update_online_users_in_json()
    return HttpResponse('OK')

@csrf_exempt
def make_gess(request):
    data = json.loads(request.body)
    print(data)
    user = Gameuser.objects.get(login=data['login'])
    card = Card.objects.get(pk=data['card_id'])
    put_card_on_table_json(user,card)
    user.state = 'gessed'
    user.save()
    update_online_users_in_json()
    return HttpResponse('OK')

@csrf_exempt
def make_bet(request):
    data = json.loads(request.body)
    user = Gameuser.objects.get(login=data['login'])
    card = Card.objects.get(pk=data['card_id'])
    put_card_on_table_json(user,card)
    user.state = 'beted'
    user.save()
    update_online_users_in_json()
    return HttpResponse('OK')