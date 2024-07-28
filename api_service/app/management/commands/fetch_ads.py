from django.core.management.base import BaseCommand
from app.parser import save_ads_to_db

class Command(BaseCommand):
    help = 'Fetch and save ads from FarPost'

    def handle(self, *args, **kwargs):
        save_ads_to_db()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved ads'))
