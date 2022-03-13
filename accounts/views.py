from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Profile
from animetitans.models import Animes_animetitans, Episode_animetitans, Categories_animetitans, Customized_Lists
from random import randint
# Create your views here.


def profile(request):

    if request.user.is_authenticated:
        render_ = 'profile.html'
        redirect_ = '/profile/'

        profile = Profile.objects.get(user=request.user)

        context = {
            # basic
            'title': 'الملف الشخصي',
            'description': 'الملف الشخصي ل  {profile.username}',
            'css': ['home.css', 'profile.css'],
            'js': ['home/main.js','profile/main.js'],
            'categories': Categories_animetitans.objects.all().order_by('category'),
            'new_upisode': Episode_animetitans.objects.all().order_by('-added_date')[:12],

            # other
            'profile': profile,
            'favorite': profile.favorite,
            'watchNow': profile.watchNow,
            'wantWatch': profile.wantWatch,
            'watched': profile.watched,

            'your_news': profile.watchNow.filter(status="مستمر"),
            'your_ep': Episode_animetitans.objects.all().order_by('-added_date')[:20],
            'username': profile.username,
            'user_her': True,
        }

        # get request
        if request.GET:
            # search
            if request.GET.get('s'):
                search = request.GET.get('s').strip().title()
                context.update({'search': search,
                                'anime_s': Animes_animetitans.objects.filter(title__istartswith=search)
                                })
                return render(request, "anime_search.html", context)
            else:
                redirect(redirect_)

        # logout
        elif request.POST.get('logout'):
            logout(request)
            return redirect('/')

        # profile picture
        elif request.FILES.get('change_profile_picture'):
            profile.profile_picture.delete()
            profile.profile_picture = request.FILES.get('change_profile_picture')
            profile.use_profile_picture = True
            profile.save()
            return redirect(redirect_)

        elif request.POST.get('delet_profile_picture'):
            if request.POST.get('delet_profile_picture') == "True":
                profile.profile_picture.delete()
                profile.use_profile_picture = False
                return redirect(redirect_)
            else:
                return redirect(redirect_)

        else:
            return render(request, render_, context)

    else:
        return redirect('/')



