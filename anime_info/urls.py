from django.urls import path
from . import views


app_name = 'anime_info'
urlpatterns = [
    path('anime-list/<slug:slug>', views.anime_info, name='anime_info'),
    
]