from django.shortcuts import render


# Create your views here.
def index(r):
    return render(r, "index.html")
def contact(r):
    return render(r, "contact.html")

def account(request):
    return render(request, 'account.html')

def donate(request):
    return render(request, 'donate.html')

def report(request):
    return render(request, 'report.html')

def single(request):
    return render(request, 'single.html')

