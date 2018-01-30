from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='home'),
    path('<int:plan_id>/', views.plan, name = 'plan'),


]