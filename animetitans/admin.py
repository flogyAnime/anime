from django.contrib import admin
from .models import Animes_animetitans, Episode_animetitans, Categories_animetitans, Customized_Lists
# Register your models here.

admin.site.register(Animes_animetitans)
admin.site.register(Episode_animetitans)
admin.site.register(Categories_animetitans)
admin.site.register(Customized_Lists)
