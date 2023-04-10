from django.urls import path
from . import views

app_name = 'second_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('second_app/', views.second_app, name='second_app'),
    path('users/', views.users, name='users')
]
