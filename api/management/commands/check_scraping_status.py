from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Check scraping status'

    def handle(self, *args, **options):
        url = 'http://127.0.0.1:8000/api/taskmanager/scraping_status/fe90d506-4006-4f47-874b-ef15cab587be'
        response = requests.get(url)
        print(response.text)
