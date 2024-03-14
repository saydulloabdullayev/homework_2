from django.shortcuts import render

def themes_list(request):
    with open('lesson.txt', 'r') as file:
        topics = file.readlines()
    return render(request, 'theme_list.html', {'topics': topics})
