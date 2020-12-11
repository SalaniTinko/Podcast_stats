from django.urls import path,include
from . import views
app_name= "pc"
urlpatterns = [
    path('', views.index,name="index"),
    path('individual-podcast/<podcast_id>/', views.Individual_Podcast,name="individual-podcast"),
    path('insert_podcast', views.insert_podcast,name="insert_podcast"),
    # podcast Home Record url
    path('population-chart/', views.population_chart, name='population-chart'),
    path('podcast-most-play/', views.podcast_most_play, name='podcast-most-play'),
    path('podcast-new-subscribe/', views.podcast_new_subscribe, name='podcast-new-subscribe'),
    path('podcast-new-plays/', views.podcost_new_plays, name='podcast-new-plays'),
    path('new-subscribe/', views.new_subscribe, name='new-subscribe'),
    path('new-plays/', views.new_plays, name='new-plays'),
    path('new-plays/', views.new_plays, name='new-plays'),
    # Podcast Individuale Record URL
    path('individuale-total-subscribe/', views.individuale_total_subscribe, name='individuale-total-subscribe'),
    path('individuale-total-plays/', views.individuale_total_plays, name='individuale-total-plays'),
    path('individuale-new-plays/', views.individuale_new_plays, name='individuale-new-plays'),
    path('individuale-new-subscribe/', views.individuale_new_subscribe, name='individuale-new-subscribe'),
]