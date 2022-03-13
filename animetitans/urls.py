from django.urls import path
from . import views

app_name = 'animetitans'
urlpatterns = [
    path('animetitans', views.animetitans, name='animetitans')
]
