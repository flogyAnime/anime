from django.db import models
from django.contrib.auth.models import User
from animetitans.models import Animes_animetitans
from cloudinary.models import CloudinaryField
# Create your models here.

def getcurrentusername(instance, filename):
    if len(filename) >= 6:
        filename = filename[-5:]
    return f"users/{instance.user.username}/profile_picture/{filename}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.CharField(max_length=200, null=True, blank=True)   #todo unique

    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True) #todo unique
    password = models.CharField(max_length=200, null=True, blank=True)
    added_date = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to=getcurrentusername)
    use_profile_picture = models.BooleanField(default=False)
    tag = models.CharField(max_length=50, null=True, blank=True, default="متابع انمي")

    # other
    favorite = models.ManyToManyField(
        Animes_animetitans, related_name='favorite', null=True, blank=True)

    watchNow = models.ManyToManyField(
        Animes_animetitans, related_name='watchNow', null=True, blank=True)

    wantWatch = models.ManyToManyField(
        Animes_animetitans, related_name='wantWatch', null=True, blank=True)

    watched = models.ManyToManyField(
        Animes_animetitans, related_name='watched', null=True, blank=True)


    def __str__(self):
        return self.user.username
