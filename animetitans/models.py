from django.db import models

# Animes
class Animes_animetitans(models.Model):
    title = models.CharField(max_length=10000)
    image = models.CharField(max_length=10000)
    trailer = models.CharField(max_length=10000, null=True, blank=True)
    rating = models.CharField(max_length=10000, null=True, blank=True)
    story = models.CharField(max_length=10000, null=True, blank=True)
    status = models.CharField(max_length=10000, null=True, blank=True)
    studio = models.CharField(max_length=10000, null=True, blank=True)
    year = models.CharField(max_length=10000, null=True, blank=True)
    duration = models.CharField(max_length=10000, null=True, blank=True)
    season = models.CharField(max_length=10000, null=True, blank=True)
    country = models.CharField(max_length=10000, null=True, blank=True)
    Type = models.CharField(max_length=100000, null=True, blank=True)
    episodes = models.CharField(max_length=10000, null=True, blank=True)
    # categories = models.CharField(max_length=1000, null=True, blank=True)
    categories = models.ManyToManyField(
        'Categories_animetitans')
    complete = models.BooleanField(default=False)
    url = models.CharField(max_length=10000, null=True, blank=True)
    slug = models.CharField(max_length=10000)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Episodes
class Episode_animetitans(models.Model):
    # anime = models.CharField(max_length=1000)
    anime = models.ForeignKey(Animes_animetitans, on_delete=models.CASCADE)
    number = models.CharField(max_length=10000)
    D_googledrive = models.CharField(max_length=10000, null=True, blank=True)
    D_mega = models.CharField(max_length=10000, null=True, blank=True)
    D_mp4upload = models.CharField(max_length=10000, null=True, blank=True)
    D_solidfiles = models.CharField(max_length=10000, null=True, blank=True)
    D_4shared = models.CharField(max_length=10000, null=True, blank=True)
    D_other = models.CharField(max_length=10000, null=True, blank=True)
    W_googledrive = models.CharField(max_length=10000, null=True, blank=True)
    W_mega = models.CharField(max_length=10000, null=True, blank=True)
    W_mp4upload = models.CharField(max_length=10000, null=True, blank=True)
    W_solidfiles = models.CharField(max_length=10000, null=True, blank=True)
    W_4shared = models.CharField(max_length=10000, null=True, blank=True)
    url = models.CharField(max_length=10000, null=True, blank=True)
    slug = models.CharField(max_length=10000)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.anime}_E{self.number}"


# Categories
class Categories_animetitans(models.Model):
    category = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


# Customized Lists
class Customized_Lists(models.Model):
    title = models.CharField(max_length=100)
    anime = models.ManyToManyField(Animes_animetitans)

    def __str__(self):
        return self.title