from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import View

def index(request):


    context = {
        'test': '123'
    }
    return render(request, 'balance/index.html', context)


def login(request):


    context = {

    }
    return render(request,'balance/login.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'balance/login.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

#            user = form.save(commit=False)
            # clean /normalized Data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
   #         user.set_password(password)
    #        user.save

            #returns User object if credentials are correct

            user = authenticate(email=email, password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('balance:index')

        return render(request,self.template_name, {'form':form})


def news(request):


    return HttpResponse("news")

def home(request):


    return HttpResponse("home")

def profile(request):


    return HttpResponse("profile")