from django.http import HttpResponse
from django.template import loader


def index(request):

    template = loader.get_template('balance/index.html')
    context = {
        'test': '123'
    }
    return HttpResponse(template.render(context, request))

def training(request,trainingsplan_id):

    template = loader.get_template('balance/training.html')
    context = {
        'id':trainingsplan_id,
    }
    return HttpResponse(template.render(context,request))

def login(request):

    template = loader.get_template('balance/login.html')
    context = {

    }
    return HttpResponse(template.render(context,request))
