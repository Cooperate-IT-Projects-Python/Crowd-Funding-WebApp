from django.shortcuts import render


# Create your views here.
def index(r):
    return render(r, "index.html")
def contact(r):
    return render(r, "contact.html")

def profile(r):
    return render(r, "profile.html")


def account(request):
    return render(request, 'account.html')

def donate(request):
    return render(request, 'donate.html')

def report(request):
    return render(request, 'report.html')

def single(request):
    return render(request, 'single.html')
def edit_profile(request):
    return render(request, 'edit_profile.html')
def change_password(request):
    return render(request, 'change_password.html')
