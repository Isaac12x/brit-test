import json
from django.conf import settings
from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = 'Load items from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Name of the JSON file to load (located in the data folder)')


    def handle(self, *args, **kwargs):
        from brit_test.app.models import Item

        filename = kwargs['filename']
        data_folder = Path(settings.BASE_DIR / 'data')
        file_path = data_folder / filename

        if not file_path.exists():
            self.stdout.write(self.style.ERROR(f'File {filename} not found in data folder'))
            return
    
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item_data in data['items']:
                Item.objects.create(
                    name=item_data['name'],
                    price=item_data['price'],
                    description=item_data.get('description', ''),
                    image=None,  # Since your JSON doesn't contain image data
                    category=item_data.get('category', 'Default')  # You can set a default category
                )
            self.stdout.write(self.style.SUCCESS('Successfully loaded all items'))