from django.core.management.base import BaseCommand
from podcast_app import views

class Command2(BaseCommand):
    def podcast_insertion(self, *args, **kwargs):
        response = views.insert_podcast()
        self.stdout.write("Counties data have been imported Now: %s" % response)