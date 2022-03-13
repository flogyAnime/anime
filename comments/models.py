from django.db import models
from accounts.models import Profile
from animetitans.models import Episode_animetitans
# Create your models here.

# Comments
class Comments(models.Model):
  episode = models.ForeignKey(Episode_animetitans, on_delete=models.CASCADE, null=True, blank=True)
  comments_id = models.CharField(max_length=100, null=True, blank=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
  comment = models.CharField(max_length=100, null=True, blank=True)
  like = models.ManyToManyField(Profile, related_name='+', null=True, blank=True)
  dislike = models.ManyToManyField(Profile, related_name='+', null=True, blank=True)
  added_date = models.DateTimeField(auto_now=True, null=True, blank=True)
  reply = models.ManyToManyField('Replys',related_name='+', null=True, blank=True)
  pin = models.BooleanField(default=False, null=True, blank=True)

  def __str__(self):
      return self.comments_id

# Replys
class Replys(models.Model):
  from_Comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, blank=True)
  comments_id = models.CharField(max_length=100, null=True, blank=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
  comment = models.CharField(max_length=100, null=True, blank=True)
  like = models.ManyToManyField(Profile, related_name='+', null=True, blank=True)
  dislike = models.ManyToManyField(Profile, related_name='+', null=True, blank=True)
  added_date = models.DateTimeField(auto_now=True, null=True, blank=True)
  pin = models.BooleanField(default=False, null=True, blank=True)

  def __str__(self):
    return self.comments_id