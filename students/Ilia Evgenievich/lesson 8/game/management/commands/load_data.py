from django.core.management.base import BaseCommand, CommandError
from game.models import Page, Images

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Load data')