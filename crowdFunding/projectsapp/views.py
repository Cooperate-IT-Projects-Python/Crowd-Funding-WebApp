from django.shortcuts import render, redirect
from audioop import avg, avgpp
from calendar import c
from datetime import date, datetime
from email import message
from re import U
import re
from tkinter import E, N
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from matplotlib.pyplot import get
from requests import post

from .models import *

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfileInfo, Project, Donation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import UserProfileInfo, Project, Donation

@login_required
def view_profile(request):
    user = request.user
    profile = UserProfileInfo.objects.get(user=user)
    projects = Project.objects.filter(user=user)
    donations = Donation.objects.filter(user=user)
    context = {
        'profile': profile,
        'projects': projects,
        'donations': donations,
    }
    return render(request, 'view_profile.html', context)

@login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         profile_form = UserProfileInfoForm(request.POST, request.FILES, instance=request.user.userprofileinfo)
#         if form.is_valid() and profile_form.is_valid():
#             form.save()
#             profile_form.save()
#             messages.success(request, f'Your profile has been updated!')
#             return redirect('view_profile')
#     else:
#         form = EditProfileForm(instance=request.user)
#         profile_form = UserProfileInfoForm(instance=request.user.userprofileinfo)
#     context = {
#         'form': form,
#         'profile_form': profile_form
#     }
#     return render(request, 'edit_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your password has been changed!')
            return redirect('view_profile')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, 'change_password.html', context)

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, f'Your account has been deleted!')
        return redirect('register')
    return render(request, 'delete_account.html')

# Create your views here.
def initFunction(r):
    pass
@never_cache
def logout(request):
    try:

        del request.session['username']

    except:
        pass

    return redirect('/users/login')
def error_404(request,exception):
    return render(request, '404.html')
def error_500(request):
    return render(request, '404.html')

