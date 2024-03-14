from urllib import request

from django.shortcuts import render



def uz(request):
    return render(request, 'Weekdays/uz_week.html')


def eng(request):
    return render(request, 'Weekdays/eng_week.html')


def rus(request):
    return render(request, 'Weekdays/rus_week.html')


def all_languages(request):
    return render(request, 'Weekdays/all_languages.html')

def month(requests):
    return render(request, 'Weekdays/month.html')

week =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Suday']
def weedays(request):
    return render(request, template_name='Weekdays/days.html',context={'Weekdays':week})