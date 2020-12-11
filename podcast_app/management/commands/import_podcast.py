from django.core.management.base import BaseCommand
from django.utils import timezone
from podcast_app import views

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response = views.insert_podcast()
        self.stdout.write("Counties data have been imported Now: %s" % response)