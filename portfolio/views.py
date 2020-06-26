from django.shortcuts import render


def home(request):
    return render(request, "portfolio/home.html", {"active": "home"})


def feed(request):
    return render(request, "portfolio/feeds.html", {"active": "feeds"})
