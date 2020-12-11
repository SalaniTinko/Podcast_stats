import datetime
import requests
import csv
from bs4 import BeautifulSoup
from django.contrib.messages.context_processors import messages

from podcast_app.models import Podcast,TotalPodcastState
'''
Requirements
$pip install requests
$pip install beautifulsoup4
'''


stats_file = 'stats_test_scrape.csv'
url = ''
rownumber = 0
def addToFile(file, stats):
    with open(file, mode='a') as stat_file:
        stat_writer = csv.writer(stat_file, delimiter=',')
        stat_writer.writerow(stats)

def getStats(url,getRowID):
    try:
        podcastData=Podcast.objects.all()
        for getPodcastUrl in podcastData:

            url = getPodcastUrl.url
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            page_title = soup.title.string # get page title tag
            page_title = str(page_title)
            page_title = page_title[:len(page_title)-26] # remove boilerplate " | Listen Free on Castbox."
            #print(page_title)

            subscribed_count = soup.find("span", "count sub_count") # get subscriber_count element
            subscribed_count = str(subscribed_count) # convert bs4 element tag to string
            subscribed_count = subscribed_count[66:len(subscribed_count)-7] # slice string for just the number
            subscribed_count = subscribed_count.replace(',', '') # remove comma
            subscribed_count = int(subscribed_count,base=10) # convert to integer for data visualisation
            #print(subscribed_count)

            played_count = soup.find("span", "count play_count") # get play_count element
            played_count = str(played_count) # convert bs4 element tag to string
            played_count = played_count[63:len(played_count)-7] # slice string for just the number
            played_count = played_count.replace(',', '') # remove comma
            played_count = int(played_count,base=10) # convert to integer for data visualisation

            statCount = [datetime.datetime.now(),page_title, subscribed_count, played_count]

            # storing record into database
            totalpodcast = TotalPodcastState.objects.create(name=page_title,total_subscribed=subscribed_count,total_played=played_count,date=datetime.datetime.now())
            totalpodcast.save()
            # new subscribe dbsstorage
            newRowID = int(totalpodcast.pk)
            print("====== new Row ID ========\t\t:",newRowID)
            newRowID -= 1
            try:
                newpodcast= TotalPodcastState.objects.get(id = newRowID)
                print(newpodcast.date)
                newSubscribed = abs(int(subscribed_count)-int(newpodcast.total_subscribed) )
                newplayed = abs(int(played_count) - int(newpodcast.total_played))
                newPodcastState = TotalPodcastState.objects.filter(pk=newRowID).update(new_subscribes=newSubscribed,new_plays=newplayed,date=datetime.datetime.now())

            except Exception as e:
                print("====query error \t\t====\t:",str(e))
            print(statCount)
            addToFile(stats_file, statCount)
    except Exception as e:
        print("models does not exist\t\t:",str(e))

def updateStatsList():
    updateStatsList.counter += 1
    tes=0
    getRowID = updateStatsList.counter
    getStats(tes,getRowID)
updateStatsList.counter = 0
updateStatsList()

