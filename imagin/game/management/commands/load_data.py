from django.core.management.base import BaseCommand, CommandError
from game.models import Page, Images

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Load data')
        for i in range(1,3):
            page = Page()
            page.title = f'Page number {i}'
            page.content = f'Page content {i}'
            page.save()
            image = Image()
            image.title = f'Image {i}'
            image.page = page
            image.save()
            print(f'Creating page {i}')

        # image = Image()
        # page = Page()
        # image.page = page