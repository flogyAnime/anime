from django.urls import path
from . import views
app_name = 'episode'
urlpatterns = [
    path('anime-list/<slug:slug>/e', views.episode, name='episode'),
]
