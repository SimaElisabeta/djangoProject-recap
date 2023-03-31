from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, WebPage, AccessRecord


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'first_app/index.html', context=date_dict)


def first_app(request):
    my_dict = {'insert_me': 'Hello from first_app/views.py!!'}
    return render(request, 'first_app/first_app_page.html', context=my_dict)
