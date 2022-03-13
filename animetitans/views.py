from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Profile
from animetitans.models import Animes_animetitans, Episode_animetitans, Categories_animetitans, Customized_Lists
from django.http import request
from django.template.defaultfilters import slugify
import animes
from deep_translator import GoogleTranslator
from random import randint

# Create your views here.


def conver(data):
    list_ = data.split(',')
    main = []
    for x in list_:
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = x.replace("'", '')
        x = x.strip()
        main.append(x)
    return main

def toEnglish(word):
    return GoogleTranslator(source='auto', target='english').translate(word)

new_animes = 0
new_episodes = 0
len_local_db_an = 0
len_local_db_ep = 0
# Save Anime
def saveAnimeToDB():
    global len_local_db_an, new_animes
    len_local_db_an = len(animes.Animes())

    for anime in animes.Animes():
        title = anime[0]
        image = anime[1]
        trailer = anime[2]
        rating = anime[3]
        story = anime[4]
        status = anime[5]
        if status != 'مستمر':
            complete = True
        studio = anime[6]
        year = anime[7]
        duration = anime[8]
        season = anime[9]
        country = anime[10]
        Type = anime[11]
        episodes = anime[12]
        categories = anime[13]
        for cat in conver(categories):
            if not Categories_animetitans.objects.filter(category=cat).exists():
                Categories_animetitans(
                    category=cat, slug=slugify(toEnglish(cat))).save()
        url = anime[14]
        slug = slugify(title)
        if not Animes_animetitans.objects.filter(slug=slug).exists():
            new_animes += 1
            data = Animes_animetitans(title=title,
                                    image=image,
                                    trailer=trailer,
                                    rating=rating,
                                    story=story,
                                    status=status,
                                    studio=studio,
                                    year=year,
                                    duration=duration,
                                    season=season,
                                    country=country,
                                    Type=Type,
                                    episodes=episodes,
                                    #  categories=categories,
                                    url=url,
                                    slug=slug,
                                    complete=complete,
                                    )
            data.save()
            anime = Animes_animetitans.objects.get(slug=slug)
            for cc in conver(categories):
                if Categories_animetitans.objects.filter(category=cc).exists():
                    anime.categories.add(
                        Categories_animetitans.objects.filter(category=cc)[0])
                    anime.save()

        else:
            if len(Animes_animetitans.objects.filter(slug=slug)) != 1:
                print("!=1")
                print(Animes_animetitans.objects.filter(slug=slug))
            else:

                update_anime = Animes_animetitans.objects.get(slug=slug)
                update_anime.rating = rating
                update_anime.save()
                update_anime.status = status
                update_anime.save()

# Save Episode
def saveEpisodeToDB():
    global len_local_db_ep, new_episodes
    len_local_db_ep = len(animes.Episodes())
    for episode in animes.Episodes():
        anime = episode[0]
        number = episode[1]
        D_googledrive = episode[2]
        D_mega = episode[3]
        D_mp4upload = episode[4]
        D_solidfiles = episode[5]
        D_4shared = episode[6]
        D_other = episode[7]
        W_googledrive = episode[8]
        W_mega = episode[9]
        W_mp4upload = episode[10]
        W_solidfiles = episode[11]
        W_4shared = episode[12]
        url = episode[13]
        slug = slugify(f'{anime}-{number}')
        if not Episode_animetitans.objects.filter(slug=slug).exists() and Animes_animetitans.objects.filter(title=anime).exists():
            new_episodes += 1
            data = Episode_animetitans(
                anime=Animes_animetitans.objects.get(title=anime),
                number=number,
                D_googledrive=D_googledrive,
                D_mega=D_mega,
                D_mp4upload=D_mp4upload,
                D_solidfiles=D_solidfiles,
                D_4shared=D_4shared,
                D_other=D_other,
                W_googledrive=W_googledrive,
                W_mega=W_mega,
                W_mp4upload=W_mp4upload,
                W_solidfiles=W_solidfiles,
                W_4shared=W_4shared,
                url=url,
                slug=slug)
            data.save()


# main
def animetitans(request):
    print(len(animes.Episodes()))
    print("##")

    if request.user.is_authenticated and request.user.username == "000000000000000000000000":
    
        render_ = 'animetitans.html'
        redirect_ = '/animetitans'

        profile = Profile.objects.get(user=request.user)

        old_animes =  Animes_animetitans.objects.all()
        old_episodes = Episode_animetitans.objects.all()

        saveAnimeToDB()
        saveEpisodeToDB()



        context = {
            # basic
            'title': 'animetitans',
            'description': '',
            'css': ['animetitans.css'],
            'js': [],

            # other
            "profile": profile,
            "old_animes" : old_animes,
            "old_episodes" : old_episodes,

            "new_animes":new_animes,
            "len_local_db_an": len_local_db_an,

            "new_episodes":new_episodes,
            "len_local_db_ep": len_local_db_ep,
        }
        return render(request, render_, context)

    else:
        return redirect('/')