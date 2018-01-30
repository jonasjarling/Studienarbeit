from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='profile'),
    path('<int:user_id>/', views.user, name = 'user'),


]