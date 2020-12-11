from django.core.management.base import BaseCommand
from podcast_app import views

class Command(BaseCommand):
    def handle4(self, *args, **kwargs):
        response = views.insert_podcast()
        self.stdout.write("Counties data have been imported Now: %s" % response)
def podcast_insertion():
    response = views.insert_podcast()
