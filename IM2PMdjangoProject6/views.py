from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Profile


def customer_profileinfopage(request):
    return render(request, "customer_profileinfopage.html")


def customer_updateregpage(request):

    return render(request, "PM/customer_updateregpage.html")


def profile_information_page_view(request):
    return render(request, 'PM/profile_information_page_customer.html')