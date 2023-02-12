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

