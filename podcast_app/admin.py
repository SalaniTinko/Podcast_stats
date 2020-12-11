import json

from django.contrib import admin
from .models import Podcast, TotalPodcastState
from django.core.serializers.json import DjangoJSONEncoder

admin.site.site_header = "Podcast Stats"
admin.site.site_title = "Podcast Stats"
admin.site.index_title = "Podcast Stats"


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "url")
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("name",)


admin.site.register(Podcast, PodcastAdmin)


class TotalPodcastStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "total_subscribed", "total_played", "date", 'new_subscribes', "new_plays")
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("name",)


admin.site.register(TotalPodcastState, TotalPodcastStateAdmin)
