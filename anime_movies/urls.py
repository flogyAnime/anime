from django.urls import path
from . import views

app_name = 'anime_movies'
urlpatterns = [
    path('anime-movies', views.anime_movies, name='anime_movies'),
]