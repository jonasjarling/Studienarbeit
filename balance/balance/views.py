from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):


    context = {
        'test': '123'
    }
    return render(request, 'balance/index.html', context)


def login(request):


    context = {

    }
    return render(request,'balance/login.html', context)

def news(request):


    return HttpResponse("news")

def home(request):


    return HttpResponse("home")

def profile(request):


    return HttpResponse("profile")