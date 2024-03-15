from django.shortcuts import render
from django.http import HttpResponse

links=f''


def themes_list(request):
    # with open('lesson.txt', 'r') as file:
    #     topics = file.readlines()
    return render(request, 'theme_list.html')


def html(request):
    return render(request, templates='html.html')

def css(request):
    return  render(request, templates='css.html')

def Bootstrap(request):
    return render(request, templates='Bootstrap.html')

def JavaScript(request):
    return  render(request, templates='JavaScript.html')