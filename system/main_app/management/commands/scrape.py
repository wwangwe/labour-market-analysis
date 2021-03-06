from django.core.management.base import BaseCommand
from main_app.threads import ScrapeThread


class Command(BaseCommand):
    help = "Triggers Data Scraping from Brighter Mondays "

    def handle(self, *args, **kwargs):
        ScrapeThread().start()
