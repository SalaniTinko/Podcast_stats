from django.db import models
import datetime
from django.utils import timezone
class Podcast(models.Model):
    name = models.CharField(max_length=30, default=True)
    url = models.CharField(max_length=120, default=True)

class TotalPodcastState(models.Model):
    newpodcast = models.ForeignKey(Podcast,on_delete=models.CASCADE,default=True,null=True,blank=True,)
    name = models.CharField(max_length=30, default=True,null=True,blank=True,)
    total_subscribed = models.IntegerField(default=True,null=True,blank=True,)
    total_played = models.IntegerField(default=True,blank=True,)
    new_subscribes = models.IntegerField(default='0',blank=True,)
    new_plays = models.IntegerField( default='0',blank=True,)
    date = models.DateTimeField(default=True,null=True,blank=True,)

# Create your models here.
