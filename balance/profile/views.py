from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

    template = loader.get_template('profile/index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def user(request, user_id):

    return HttpResponse("Hier sehen Sie User %s." % user_id)