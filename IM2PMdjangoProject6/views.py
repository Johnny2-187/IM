from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Profile


def profileinfopage(request):
    return render(request, "profileinfopage.html")


def profile(request):

    return render(request, "PM/profile.html")
