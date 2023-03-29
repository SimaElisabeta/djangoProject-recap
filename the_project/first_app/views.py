from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')


def first_app(request):
    my_dict = {'insert_me': 'Hello from first_app/views.py!!'}
    return render(request, 'first_app/first_app_page.html', context=my_dict)
