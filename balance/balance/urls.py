"""balance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = (

   # path('training/', views.training, name='training'),
    path('login/', views.login, name='login'),
    path('training/', include('training.urls')),
    path('statistic/', include('statistic.urls')),
    path('news/', views.news, name='news'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.UserFormView.as_view(), name='register'),

    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

)
