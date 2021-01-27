from django.core.management.base import BaseCommand, CommandError
from game.models import Page, Images
from django.core.files import File
from imagin.settings import BASE_DIR

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Load data')

        print('Clear data')
        Page.objects.all().delete()
        Images.objects.all().delete()
        
        for i in range(1,19):
            image = Images()
            image.title = f'Image {i}'
            filepath = f'{BASE_DIR}/static/images/{i}.jpg'
            with open(filepath, 'rb') as doc_file:
                image.image.save(f'{i}.jpg', File(doc_file), save=True)
            
            image.save()
            print(f'Creating page {i}')

        # image = Image()
        # page = Page()
        # image.page = page