from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

    template = loader.get_template('training/index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def plan(request, plan_id):

    return HttpResponse("Hier sehen Sie Plan %s." % plan_id)