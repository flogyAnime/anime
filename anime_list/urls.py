from django.urls import path
from . import views

app_name = 'anime_list'
urlpatterns = [
    path('anime-list', views.anime_list, name='anime_list'),
]