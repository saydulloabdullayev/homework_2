# from os import name
#
# from django import urls
#
# from weekdays import views
#
# urlpatterns = [urls.path('', views.index, name='index')]
#
from django.urls import path

import weekdays
from . import views
from .views import uz,eng,rus,month,weedays

urlpatterns = [
    path("uz/", uz),
    path("en/", eng),
    path("ru/", rus),
]


