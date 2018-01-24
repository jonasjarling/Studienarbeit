from django.http import HttpResponse
from django.template import loader


def index(request):

    template = loader.get_template('balance/index.html')
    context = {
        'test': '123'
    }
    return HttpResponse(template.render(context, request))