from django.shortcuts import render


# Create your views here.
def index(r):
    return render(r, "index.html")
def contact(r):
    return render(r, "contact.html")
