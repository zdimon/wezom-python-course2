from django.core.management.base import BaseCommand, CommandError
from game.models import Card2User, Gameuser, Card
from django.core.files import File
from imagin.settings import BASE_DIR
json_path = f'{BASE_DIR}/static/data.json'
json_tpl = '{"table": [], "users": [], "status": "start", "association": ""}'

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Clear data')

        print('Clear data')
        Card2User.objects.all().delete()
        for u in Gameuser.objects.all():
            u.state = 'bettor'
            u.save()
        for c in Card.objects.all():
            c.on_hand = False
            c.save()
        with open(json_path, 'w') as file:
            file.write(json_tpl)