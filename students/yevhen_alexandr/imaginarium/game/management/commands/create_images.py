from django.core.management.base import BaseCommand, CommandError
from game.models import Image
from django.core.files import File
from imaginarium.settings import BASE_DIR
import os

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        imagepath = f'{BASE_DIR}/static/images'
        image_list = os.listdir(imagepath)
        images = Image.objects.all()

        for image_file in image_list:
            if image_file[-4:] == '.jpg':
                title = image_file[:-4]
                if not images.filter(title=title):
                    image = Image(title=title)

                    with open(os.path.join(imagepath, image_file), 'rb') as src_file:
                        image.image.save(f'{title}.jpg', File(src_file), save=True)
                
                    image.save()
                    print(f'{title} image created...')
