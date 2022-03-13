from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('anime-list/<slug:slug>/comments', views.Comments_main, name='Comments_main'),
    path('anime-list/<slug:slug>/Replys', views.Reply, name='Reply'),
]