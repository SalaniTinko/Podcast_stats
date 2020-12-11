from django.db.models.functions import Length
from django.http import HttpResponse, request
from django.shortcuts import render
import csv
from django.http import JsonResponse
from django.db import connection
import datetime
from django.utils import timezone
from .models import Podcast,TotalPodcastState

def index(requests):
    all_podcast=TotalPodcastState.objects.all()
    context = {
        'all_podcast':all_podcast
    }
    return render(requests, 'index.html',context)


def Individual_Podcast(requests,podcast_id):
    print("====== podcast_id =======\t\t:",podcast_id)
    ind_podcast=TotalPodcastState.objects.filter(name=str(podcast_id))
    record_id=0
    for ip in ind_podcast:
        print("====== ind posd=====\t\t\t",ip.name)
        record_id= ip.id
    all_podcast=TotalPodcastState.objects.all()

    requests.session['record_id'] = str(record_id)

    record_id = requests.session.get("record_id")
    print("session\t\t\t:",record_id)


    context = {
        'all_podcast':all_podcast,
        'record_id':record_id,
        'record_id':record_id
    }
    return render(requests, 'individual_podcast.html',context)


def insert_podcast():
    path = "template/csv_files/"
    a = 0
    fname = "template/csv_files/stats_test_scrape.csv"
    try:
        Podcast_record = Podcast.objects.all()

        with open(fname, 'r') as file:

            data = csv.reader(file)
            count = 0
            for key in data:
                name = key[0]
                url = key[1]
                print(name)
                if Podcast_record:
                    podcastData = Podcast.objects.filter(name=name).update(name=name, url=url)
                else:
                    for key in data:
                        podcastData = Podcast.objects.create(name=key[0], url=key[1])
                        podcastData.save()
    except Exception as e:
        print("=====model error==\t\t:",str(e))

    return HttpResponse("success")


def population_chart(request):

    totalPodcastStateQuerySet  = TotalPodcastState.objects.all().order_by('-total_subscribed')[:10]
    # list for graph maping record
    labels = []
    data = []
    # graph 1 // podcast with most subscribe
    for tpc in totalPodcastStateQuerySet:
        data.append(tpc.total_subscribed)
        labels.append(tpc.name)
    return JsonResponse(data= {
        "labels": labels,
        "data": data
    })
def podcast_most_play(request):

    totalPodcastStateQuerySet  = TotalPodcastState.objects.all().order_by('-total_played')[:10]
    # list for graph maping record
    labels = []
    data = []
    # graph 1 // podcast with most subscribe
    for tpc in totalPodcastStateQuerySet:
        data.append(tpc.total_played)
        labels.append(tpc.name)
    return JsonResponse(data= {
        "labels": labels,
        "data": data
    })

def podcast_new_subscribe(request):

    totalPodcastStateQuerySet  = TotalPodcastState.objects.all().order_by('-new_subscribes')[:10]
    # list for graph mapping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        data.append(npc.new_subscribes)
        labels.append(npc.name)
    return JsonResponse(data= {
        "labels": labels,
        "data": data
    })


def podcost_new_plays(request):

    totalPodcastStateQuerySet  = TotalPodcastState.objects.all().order_by('-new_plays')[:10]
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        data.append(npc.new_plays)
        labels.append(npc.name)
    return JsonResponse(data= {
        "labels": labels,
        "data": data
    })

def new_subscribe(request):

    totalPodcastStateQuerySet = TotalPodcastState.objects.values('new_subscribes', 'date').order_by('date')[:10]
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        data.append(npc['new_subscribes'])
        labels.append(npc['date'])
    return JsonResponse(data={
        "labels": labels,
        "data": data
    })



def new_plays(request):

    totalPodcastStateQuerySet  = TotalPodcastState.objects.values('new_plays','date').order_by('date')[:10]
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        data.append(npc['new_plays'])
        labels.append(npc['date'])
    return JsonResponse(data= {
        "labels": labels,
        "data": data
    })

# INDIVIDUALS Graph RECORDS
# individuale

def individuale_total_subscribe(requests):

    record_id = requests.session.get("record_id")
    totalPodcastStateQuerySet  = TotalPodcastState.objects.filter(id=record_id)
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        print("===totalPodcastStateQuerySet=\t\t:",npc.new_plays)
        data.append(npc.new_subscribes)
        labels.append(npc.date)
    return JsonResponse(data= {
        "labels": labels,
        "data": data
    })




def individuale_total_plays(requests):
    record_id = requests.session.get("record_id")
    totalPodcastStateQuerySet = TotalPodcastState.objects.filter(id=record_id)
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        print("===totalPodcastStateQuerySet=\t\t:", npc.new_plays)
        data.append(npc.total_played)
        labels.append(npc.date)
    return JsonResponse(data={
        "labels": labels,
        "data": data
    })


def individuale_new_plays(requests):
    record_id = requests.session.get("record_id")
    totalPodcastStateQuerySet = TotalPodcastState.objects.filter(id=record_id)
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        print("===totalPodcastStateQuerySet=\t\t:", npc.new_plays)
        data.append(npc.new_plays)
        labels.append(npc.date)
    return JsonResponse(data={
        "labels": labels,
        "data": data
    })


def individuale_new_subscribe(requests):
    record_id = requests.session.get("record_id")
    totalPodcastStateQuerySet = TotalPodcastState.objects.filter(id=record_id)
    # list for graph maping record
    labels = []
    data = []
    for npc in totalPodcastStateQuerySet:
        print("===totalPodcastStateQuerySet=\t\t:", npc.new_plays)
        data.append(npc.new_subscribes)
        labels.append(npc.date)
    return JsonResponse(data={
        "labels": labels,
        "data": data
    })