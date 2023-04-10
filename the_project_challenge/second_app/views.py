from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')


def second_app(request):
    my_dict = {'insert_me': 'Hello from second_app/views.py!!'}
    return render(request, 'second_app/second_app_page.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'access_users': user_list}
    return render(request, 'second_app/users.html', context=user_dict)
