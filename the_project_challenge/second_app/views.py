from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')


def second_app(request):
    my_dict = {'insert_me': 'Hello from second_app/views.py!!'}
    return render(request, 'second_app/second_app_page.html', context=my_dict)
