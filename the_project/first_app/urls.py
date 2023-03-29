from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('first_app/', views.first_app, name='first_app')
]
