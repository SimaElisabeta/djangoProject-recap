from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

names = ['Feb', 'Mar', 'Apr']
sections = ['1', '2', '3']


def index(request):
    return render(request, 'basic_app/index.html', {'names': names})


def relative(request, look_name, look_section):
    current_section = look_section
    current_name = look_name
    if look_name in names and look_section in sections:
        return render(request, 'basic_app/relative_url_templates.html', {'names': names,
                                                                         'sections': sections,
                                                                         'active_tab': current_name,
                                                                         'active_section': current_section})
    else:
        return HttpResponse('Error 404, Page does not exist!')


def other(request):
    return render(request, 'basic_app/other.html', {'names': names})
