from django.urls import path
from . import views

# TEMPLATE TAGGING - setting a global name for the app
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:look_name>/<str:look_section>/', views.relative, name='relative'),
    path('other', views.other, name='other')
]
