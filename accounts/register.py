from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.models import Profile
from random import randint

context = {}
def register(request, render_, redirect_):
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
                    return redirect(redirect_)
                else:
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
                return redirect(redirect_)
            else:   # if was information is not correct
                context.update({
                    'old_email': True,  # show notification
                })
                return render(request, render_, context)

        else:
            user = User.objects.create_user(
                username=id_user, password=password_sign)
            Profile(user=user, id_user=id_user, username=FullName, email=email_sign,
                    password=password_sign).save()  # create user profile
            login(request, user)
            return redirect(redirect_)

    else:   # if other post request
        return redirect(redirect_)
