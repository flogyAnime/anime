from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.models import Profile
from animetitans.models import Animes_animetitans, Episode_animetitans, Categories_animetitans, Customized_Lists
from random import randint


def home(request):
    render_ = 'home.html'
    redirect_ = '/'

    # main functions
    def register_context(profile):  #register_context
        context.update({
        'your_news':profile.watchNow.filter(status="مستمر"),
        'your_ep':Episode_animetitans.objects.all().order_by('-added_date')[:20],
        'username': profile.username,
        'user_her': True,
    })

    context = {
        # basic 
        'title': 'anime flogy',
        'description': 'مشاهدة وتحميل جميع انميات المفضلة مجانا مجانا على موقع Anime Flogy',
        'css': ['home.css'],
        'js': ['home/main.js'],
        'categories': Categories_animetitans.objects.all().order_by('category'),
        'new_upisode': Episode_animetitans.objects.all().order_by('-added_date')[:12],

        # others
        'anime': Animes_animetitans.objects.all(),
        'best': Animes_animetitans.objects.order_by('-rating')[:12],
        'this_season': Animes_animetitans.objects.order_by('-rating').filter(season='شتاء 2022')[:12],
        'recommended_animes': Customized_Lists.objects.get(title='Recommended Animes'),
    }
    if request.user.is_authenticated:   
        profile = Profile.objects.get(user=request.user)
        register_context(profile)

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

    # post request
    elif request.POST:
        # login
        if request.POST.get('email_log') and request.POST.get('password_log'):
            email_log = request.POST.get('email_log')   # email
            password_log = request.POST.get('password_log')  # password

            # if email is already exists
            if Profile.objects.filter(email=email_log).exists():
                # if the user is already exists
                if Profile.objects.filter(email=email_log, password=password_log).exists():
                    main_username = Profile.objects.get(
                        email=email_log, password=password_log).id_user  # get main_username
                    # check the information
                    user = authenticate(
                        request, username=main_username, password=password_log)

                    if user:  # if was information is correct
                        login(request, user)
                        profile = Profile.objects.get(
                            email=email_log, password=password_log)
                        register_context(profile)
                        context.update({
                            'welcome_again': True,  # show notification
                        })
                        return render(request, render_, context)
                    else:  # ! error, user not found in django users
                        return redirect(redirect_)
                else:  # if the user is not exists
                    context.update({
                        'wrong_password': True,  # show notification
                    })
                    return render(request, render_, context)
            else:  # if email is not exists
                context.update({
                    'error_username': True,  # show notification
                })
                return render(request, render_, context)

        # signup
        elif request.POST.get('FullName') and request.POST.get('email_sign') and request.POST.get('password_sign'):
            FullName = request.POST.get('FullName')  # username
            email_sign = request.POST.get('email_sign')  # email
            password_sign = request.POST.get('password_sign')   # password

            while True:  # generation a new user id
                id_user = str(randint(1, 100000000000000000000000)).zfill(24)
                if not Profile.objects.filter(id_user=id_user).exists():
                    break

            # if email already exists
            if Profile.objects.filter(email=email_sign).exists():
                main_username = Profile.objects.get(
                    email=email_sign).id_user   # get id_user from profile
                # check the information
                user = authenticate(
                    request, username=main_username, password=password_sign)
                if user:    # if was information is correct
                    login(request, user)
                    profile = Profile.objects.get(
                        email=email_sign, password=password_sign)
                    register_context(profile)
                    context.update({
                        'welcome_again': True,  # show notification
                    })
                    return render(request, render_, context)
                else:   # if was information is not correct
                    context.update({
                        'old_email': True,  # show notification
                    })
                    return render(request, render_, context)

            else:
                print('#0')
                user = User.objects.create_user(
                    username=id_user, password=password_sign)
                print('#1')
                Profile(user=user, id_user=id_user, username=FullName, email=email_sign,
                        password=password_sign).save()  # create user profile
                print('#2')
                login(request, user)
                print('#3')
                profile = Profile.objects.get(
                    email=email_sign, password=password_sign)
                print('#4')
                register_context(profile)
                print('#5')
                context.update({
                    'new_user': True,  # show notification
                })
                print('#6')
                return render(request, render_, context)

        else:   # if other post request
            return redirect(redirect_)
    else:
        return render(request, render_, context)
